# Paper Reading Skills

[English](#english) | [中文](#中文)

---

## 中文

一套面向 AI 编程助手（Claude Code / WorkBuddy / 昆仑小智 等）的**论文阅读与科研工作流技能包**。覆盖从"找论文 → 读论文 → 横向综合 → 写论文 → 选期刊"的完整链路。

每个技能是一个独立目录，按需拷贝到你的 skills 目录即可使用，无需安装全部。

---

## 技能清单

| 目录 | 名称 | 一句话用途 |
|---|---|---|
| `paper-reading/` | paper-reading | 单篇论文精读/速读/批判/关联，提取作者原图，生成 8 要素笔记 |
| `batch-paper-reading/` | batch-paper-reading | 整文件夹 20–100+ 篇 PDF 的多代理并行精读与报告装配 |
| `research-literature-synthesis/` | research-literature-synthesis | 多篇论文横向综合：路线演进、共识/分歧、Real Gap、实验设计 |
| `paper-pdf-download/` | paper-pdf-download | 按标题/DOI 从 Unpaywall/PMC/bioRxiv 等合法渠道下载开放获取 PDF |
| `academic-paper-writing/` | academic-paper-writing | 英文论文写作全流程：框架契约、分章写作、语言质检、LaTeX 化 |
| `journal-selection/` | journal-selection | 期刊投稿选刊评估：竞品扫描、分区/IF 核实、篇幅与周期匹配 |
| `long-doc-reading-report/` | long-doc-reading-report | 把长篇 Word/PDF 方案文档转成分层可折叠 HTML 阅读报告 |

## 快速开始

### 安装单个技能

```bash
# 克隆本仓库
git clone https://github.com/<你的用户名>/paper-reading-skills.git
cd paper-reading-skills

# 以 Claude Code 为例：把需要的技能目录拷贝到用户级 skills 目录
cp -r paper-reading ~/.claude/skills/

# 或 WorkBuddy / 其他兼容客户端（路径因客户端而异）
cp -r paper-reading ~/.workbuddy/skills/
```

Windows（PowerShell）：

```powershell
Copy-Item -Recurse paper-reading "$HOME\.claude\skills\"
```

安装后重启你的 AI 客户端，让它重新索引 skills。

### 安装全部

```bash
# Claude Code
cp -r paper-reading batch-paper-reading research-literature-synthesis \
      paper-pdf-download academic-paper-writing journal-selection \
      long-doc-reading-report ~/.claude/skills/
```

### 在 Cursor 中使用

把技能目录复制到 `~/.cursor/skills/`，重启 Cursor 即可。SKILL.md 头部的 `name` + `description` 是触发器，不要删除或改成纯中文简介。

### 不安装也能用（任意 AI 网页版）

打开任意技能的 `SKILL.md`，全选复制全文，粘到豆包/ChatGPT/Claude/Kimi 等对话的第一条消息，末尾加一句"明白了就回复：已加载"。之后正常上传 PDF 或提需求即可。

## 使用示例

```text
精读这篇 PDF：~/papers/nicheformer.pdf，输出 8 要素笔记，框架图用作者原图
```

```text
这个文件夹有 30 篇单细胞扰动预测论文，用 batch-paper-reading 做批量精读
```

```text
基于已读完的 8 篇笔记，做技术路线梳理 + 共识分歧分析 + Real Gap 挖掘
```

```text
帮我下载 Squidiff 这篇论文（DOI: 10.1038/s41592-025-02877-y）
```

```text
这篇综述投什么期刊合适？目标 Nature 子刊或 Briefings in Bioinformatics
```

## 依赖

大部分技能只需 AI 客户端本身。以下技能有额外依赖：

| 技能 | 依赖 |
|---|---|
| paper-reading | Python 3 + PyMuPDF（`pip install pymupdf`） |
| batch-paper-reading | Python 3 + PyMuPDF + PIL（`pip install pymupdf pillow`） |
| paper-pdf-download | Python 3 + pypdf + fontTools（`pip install pypdf fonttools`）；脚本仅需标准库 |

## 许可证

本仓库整体采用 **MIT License**，见根目录 [LICENSE](LICENSE)。

其中 `research-literature-synthesis/` 目录基于 [Aclexoe/research-literature-analysis](https://github.com/Aclexoe/research-literature-analysis)（MIT）改造，保留了原作者版权声明（见该目录下的 `LICENSE`）。

## 贡献

欢迎 Issue 与 Pull Request。提交新技能时请确保：

- 目录名为小写连字符格式（kebab-case）；
- `SKILL.md` 包含合法的 YAML frontmatter（`name` + `description`）；
- 不含任何个人隐私信息或硬编码的本机路径。

---

## English

A collection of **academic paper reading and research workflow skills** for AI coding assistants (Claude Code, WorkBuddy, Cursor, and other compatible clients). Covers the full pipeline: find papers → read papers → synthesize across papers → write papers → select journals.

Each skill is a standalone directory. Copy only what you need into your skills directory—no need to install all of them.

---

## Skills Overview

| Directory | Name | What it does |
|---|---|---|
| `paper-reading/` | paper-reading | Single-paper deep read / triage / critique / related-work; extracts author figures; produces structured 8-element notes |
| `batch-paper-reading/` | batch-paper-reading | Multi-agent parallel deep reading of 20–100+ PDFs in a folder, with report assembly |
| `research-literature-synthesis/` | research-literature-synthesis | Cross-paper synthesis: research routes, evolution chains, consensus vs. disagreement, Real Gap mining, experiment design |
| `paper-pdf-download/` | paper-pdf-download | Download legal open-access PDFs by title/DOI from Unpaywall, PMC, bioRxiv, etc. |
| `academic-paper-writing/` | academic-paper-writing | Full English paper writing workflow: framework contract, section-by-section writing, language QC, LaTeX conversion |
| `journal-selection/` | journal-selection | Journal submission evaluation: competitor scan, IF/quartile verification, page limit and turnaround matching |
| `long-doc-reading-report/` | long-doc-reading-report | Convert long Word/PDF technical documents into layered, collapsible HTML reading reports |

## Quick Start

### Install a single skill

```bash
# Clone this repository
git clone https://github.com/XPgogogo/paper-reading-skills.git
cd paper-reading-skills

# Claude Code: copy the skill you need to your user-level skills directory
cp -r paper-reading ~/.claude/skills/

# WorkBuddy / other compatible clients (path varies by client)
cp -r paper-reading ~/.workbuddy/skills/
```

Windows (PowerShell):

```powershell
Copy-Item -Recurse paper-reading "$HOME\.claude\skills\"
```

Restart your AI client after installation so it re-indexes skills.

### Install all skills

```bash
# Claude Code
cp -r paper-reading batch-paper-reading research-literature-synthesis \
      paper-pdf-download academic-paper-writing journal-selection \
      long-doc-reading-report ~/.claude/skills/
```

### Use in Cursor

Copy the skill directory to `~/.cursor/skills/` and restart Cursor. The `name` + `description` in SKILL.md frontmatter are the trigger—do not delete or translate them.

### Use without installing (any web-based AI)

Open any skill's `SKILL.md`, copy the full text, and paste it as the first message in your conversation with ChatGPT, Claude, Kimi, Doubao, etc. Append "Reply 'loaded' when ready." Then upload your PDF or describe your need as usual.

## Usage Examples

```text
Deep read this PDF: ~/papers/nicheformer.pdf — output 8-element notes, use the author's original architecture figure
```

```text
This folder has 30 single-cell perturbation prediction papers. Use batch-paper-reading for parallel deep reading.
```

```text
Based on the 8 papers I've already read, do a research route synthesis + consensus/disagreement analysis + Real Gap mining.
```

```text
Download the Squidiff paper for me (DOI: 10.1038/s41592-025-02877-y)
```

```text
Which journal should I submit this review to? Targeting Nature sub-journals or Briefings in Bioinformatics.
```

## Dependencies

Most skills only need the AI client itself. The following have extra dependencies:

| Skill | Dependencies |
|---|---|
| paper-reading | Python 3 + PyMuPDF (`pip install pymupdf`) |
| batch-paper-reading | Python 3 + PyMuPDF + PIL (`pip install pymupdf pillow`) |
| paper-pdf-download | Python 3 + pypdf + fontTools (`pip install pypdf fonttools`); bundled script uses only stdlib |

## License

This repository is released under the **MIT License**. See [LICENSE](LICENSE).

The `research-literature-synthesis/` directory is adapted from [Aclexoe/research-literature-analysis](https://github.com/Aclexoe/research-literature-analysis) (MIT). The original copyright notice is preserved in that directory's `LICENSE` file.

## Contributing

Issues and Pull Requests are welcome. When submitting a new skill, please ensure:

- Directory name uses kebab-case (lowercase letters, digits, and hyphens);
- `SKILL.md` contains valid YAML frontmatter (`name` + `description`);
- No personal information or hardcoded local paths.
