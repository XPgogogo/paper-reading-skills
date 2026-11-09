#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PMC PoW 门破解下载器

用法: python pmc_pow_download.py <PDF_URL> <输出路径>

原理: pmc.ncbi.nlm.nih.gov 的 PDF 请求返回 "Preparing to download..." 页，
内嵌 POW_CHALLENGE 与 POW_DIFFICULTY。算法（逆向自 pow-o51sQKbL.js）：
    找 nonce 使 SHA-256(challenge + str(nonce)) 的十六进制以 "0"*difficulty 开头
    cookie cloudpmc-viewer-pow = f"{challenge},{nonce}"
带 cookie 重新请求即得 PDF。难度 4 时 Python 暴力数万次，秒级完成。
"""
import hashlib
import re
import sys
import urllib.request
from http.cookiejar import Cookie, CookieJar

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/130.0 Safari/537.36")


def solve_pow(challenge: str, difficulty: int) -> int:
    prefix = "0" * difficulty
    nonce = 0
    while True:
        if hashlib.sha256((challenge + str(nonce)).encode()).hexdigest().startswith(prefix):
            return nonce
        nonce += 1


def download(pdf_url: str, out_path: str) -> bool:
    jar = CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
    opener.addheaders = [("User-Agent", UA)]

    resp = opener.open(pdf_url, timeout=60)
    ctype = resp.headers.get("Content-Type", "")
    data = resp.read()
    if data[:5] == b"%PDF-" or ctype.startswith("application/pdf"):
        open(out_path, "wb").write(data)
        print(f"[直接成功] {out_path} ({len(data)/1024:.0f} KB)")
        return True

    page = data.decode("utf-8", errors="replace")
    m = re.search(r'const POW_CHALLENGE = "([^"]+)"', page)
    d = re.search(r'const POW_DIFFICULTY = "(\d+)"', page)
    if not m:
        print(f"[失败] 未找到 PoW 挑战，页面前 300 字符: {page[:300]}")
        return False
    challenge, difficulty = m.group(1), int(d.group(1)) if d else 4
    print(f"挑战: {challenge[:24]}... | 难度: {difficulty}")

    nonce = solve_pow(challenge, difficulty)
    print(f"解出 nonce={nonce}")

    # 从最终 URL 的 host 推断 cookie 域
    host = urllib.request.urlparse(resp.geturl()).hostname or "pmc.ncbi.nlm.nih.gov"
    domain = "." + ".".join(host.split(".")[-2:])
    jar.set_cookie(Cookie(
        version=0, name="cloudpmc-viewer-pow", value=f"{challenge},{nonce}",
        port=None, port_specified=False, domain=domain, domain_specified=True,
        domain_initial_dot=True, path="/", path_specified=True, secure=False,
        expires=None, discard=False, comment=None, comment_url=None,
        rest={}, rfc2109=False))

    req = urllib.request.Request(pdf_url, headers={"User-Agent": UA})
    data2 = opener.open(req, timeout=300).read()
    print(f"二次响应: {len(data2)} bytes | {resp.headers.get('Content-Type')}")
    if data2[:5] == b"%PDF-":
        open(out_path, "wb").write(data2)
        print(f"[成功] {out_path} ({len(data2)/1024:.0f} KB)")
        return True
    print(f"[失败] 仍非 PDF，前 200 字节: {data2[:200]}")
    return False


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    sys.exit(0 if download(sys.argv[1], sys.argv[2]) else 2)
