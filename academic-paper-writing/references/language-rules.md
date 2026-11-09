# 语言规则与质检标准（Step 3 执行）

分三层执行：四条硬规则（一票否决）→ 常规规范 → 文风一致性。

---

## 一、四条硬规则（一票否决，成稿前强制通过）

### 规则 1：禁用 em dash（—、——、 -- ）

**执行**：全文正则扫描 `—`、`——`、` -- `；一律改写为逗号、括号或拆句。

改写示例：
- ❌ `Our method — which builds on attention — achieves ...`
- ✅ `Our method, which builds on attention, achieves ...`
- ❌ `The results are significant — they improve accuracy by 5%.`
- ✅ `The results are significant: they improve accuracy by 5%.`

### 规则 2：禁止无故造词

**执行**：提取存疑复合词/自造词（连字符超过 2 个的复合、词典无收录的自造名词化），对照领域标准词表裁决。

**白名单（公认术语，直接放行）**：
single-cell, scRNA-seq, multi-modal, multimodal, self-supervised, foundation model, fine-tune, fine-tuning, zero-shot, few-shot, pre-train, pre-training, downstream, end-to-end, state-of-the-art, large-scale, cross-attention, prompt-tuning, graph neural network, cell-type annotation, perturbation prediction, marker gene, batch effect, embedding, tokenizer, scalable, interpretable

**裁决标准**：PubMed/arXiv 高频可见（>100 篇）→ 放行；仅本文作者使用 → 改写为标准表达。
改写示例：
- ❌ `our multi-granularity-aware-attention-driven framework` → ✅ `our framework with multi-granularity attention`
- ❌ `the collaborativeness of nodes` → ✅ `the degree of collaboration among nodes`

### 规则 3：标准学术词汇，禁口语化

**黑名单替换表**：

| 口语化 | 学术等价 |
|--------|----------|
| a lot of / lots of | numerous, substantial, considerable |
| get | obtain, acquire, receive |
| big | substantial, considerable, large-scale |
| look at | examine, investigate, inspect |
| find out | determine, identify, discover |
| kind of / sort of | approximately, to some extent |
| thing | component, aspect, element, factor |
| stuff | material, content, data |
| good | effective, favorable, superior |
| bad | adverse, suboptimal, unfavorable |
| check | verify, validate, examine |
| help | facilitate, assist, enable |
| show up | emerge, manifest |
| use | employ, utilize, adopt |
| do | perform, conduct, carry out |
| make | construct, generate, produce |
| really / very | 删除或换量化表述（substantially, markedly） |
| so | therefore, consequently, hence |
| also | additionally, moreover（忌段首连用） |
| but | however, whereas, nevertheless |
| now | currently, to date |
| a bit | marginally, slightly |

### 规则 4：去 AI 写作痕迹

**禁词表**：
delve, crucial, pivotal, landscape (作比喻), tapestry, foster, underscore, unleash, harness (慎用), realm, embark, paramount, instrumental, noteworthy (段首), multifaceted, intricate (描述系统), seamless, holistic, robust (泛用无实义时), intricate interplay, myriad

**禁句式**：
- ❌ `X is not just Y, it is Z` / `not only ... but also ...`（排比堆叠）
- ❌ 段首 Moreover / Furthermore / Additionally 连续两段以上
- ❌ 三段式排比（`To A. To B. To C.`）
- ❌ `In conclusion, X represents a significant step forward.`（空洞收尾）
- ❌ `In today's rapidly evolving world of ...`（开头宏大叙事）
- ❌ `It is worth noting that` / `It is important to mention that`（无信息量的填充语，直接删）
- ❌ `plays a crucial role in`（高频 AI 搭配，换具体动词）
- ❌ `aim to` / `is designed to` 连续使用（一段内多次出现）

**改写策略**：AI 痕迹句 → 换具体主语 + 强动词 + 事实内容。

---

## 二、常规规范检查

### 时态一致性
- 领域事实、本文方法：现在时
- 前人工作：过去时（proposed）或现在完成时（has explored）
- 本文实验过程：过去时（was trained, we conducted）
- 图表报告：现在时（Table 2 shows）
- 全文同类场景时态统一，禁止同一段内漂移

### Hedging 适度性
- 过度 hedging（may/might/might/could possibly 堆叠）削弱论点 → 删减至单层
- 过度强断言越证据（数据只支持 5% 提升却写 significantly outperforms）→ 加限定或量化
- 检查每个结论句：断言强度与证据强度匹配

### 术语与缩写一致性
- 每个缩写首现给全称，如 `graph neural network (GNN)`
- 全文一词到底：确定 dataset 还是 corpus、model 还是 network，不混用
- 与框架契约术语表核对

### 图表引用格式（按 profile）
- 正文缩写：Fig. 3、Table 2（P1/P2/P4）；Figure 全拼（P3 常见）
- 句首不缩写：`Figure 3 shows ...`（或按 profile）
- 每图每表至少被正文引用一次

### 引用密度
- 每个 gap 论断、每个"现有方法..."概括处有引用支撑
- 标注两类问题段落：有论点无引用（引用缺失）；单句堆砌 5+ 引用（citation dumping，建议拆分评述）

---

## 三、文风一致性检查（按 Step 0 文风画像）

逐章比对文风画像五维度：

| 检查项 | 方法 |
|--------|------|
| 叙述节奏 | 段落长度是否落在该刊习惯区间；Intro 展开速度是否匹配 |
| 句式复杂度 | 平均句长、从句嵌套深度是否在区间内 |
| 语态比例 | 主动/被动比例是否符合 profile |
| 贡献陈述方式 | bullet（P1）vs 行文（P2/P4）是否符合 |
| hedging 强度 | 强断言（P1）vs 克制（P2/P3）vs 叙事（P4）是否匹配 |

发现"读起来像别的刊"的段落：标注所在章节与行号，按文风画像改写，改写前后对照呈现给用户。

---

## 四、质检报告格式（中文输出）

```markdown
# 质检报告
## 1. 硬规则扫描结果
| 规则 | 命中数 | 位置示例 | 修改方式 |
（逐条列出，改写前 → 改写后）
## 2. 常规规范
（时态/hedging/术语/图表引用/引用密度，逐项结论 + 问题定位）
## 3. 文风一致性
（偏离段落定位 + 改写对照）
## 4. 修改后全文
（完整 Markdown）
```

经用户确认后，方可进入 Step 4 LaTeX 化。
