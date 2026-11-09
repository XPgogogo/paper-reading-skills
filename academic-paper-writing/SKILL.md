---
name: academic-paper-writing
description: Use when 科研人员需要撰写、翻译、润色或修改英文学术论文时（触发词：写英文论文、论文写作、写 Introduction、写 Abstract、写 Related Work、写 Methodology、润色论文、论文翻译成英文、中文稿改英文、投稿、cover letter、rebuttal、response to reviewers、审稿意见修改、审稿人模拟、论文质检、LaTeX 化）；目标期刊覆盖 AI/ML CCF 类会议期刊（NeurIPS/ICML/ICLR/AAAI/IJCAI/TPAMI 等）、生信专业刊（Bioinformatics/Genome Biology 等）、Nature 及其子刊。覆盖从框架规划、分章写作、语言质检、LaTeX 工程化到投稿支撑的全流程。不适用于中文论文与学位论文。
agent_created: true
---

# 学术论文写作（academic-paper-writing）

## 概述

英文学术论文写作全流程助手。核心工作流：**初始化 → 框架规划 → 分章写作(Markdown) → 强制质检 → LaTeX 化 → 投稿支撑**，文献辅助贯穿全程。

## 七条设计原则（元规则，全程生效）

1. **框架先行，契约驱动**——未经用户确认框架契约，绝不动笔写任何章节
2. **用户拍板制**——四道确认关卡：框架契约 → 关键章节逐段 → 质检报告 → LaTeX 模板；任一关卡未确认不推进
3. **语言硬规则一票否决**——四条硬规则（见 `references/language-rules.md`）在质检环节强制执行，不通过不算成稿
4. **Markdown 先行，LaTeX 后置**——内容定型后再排版，内容与格式解耦
5. **期刊 profile 分治**——结构规范与文风基准按 profile 参数化（见 `references/profiles.md`），不为单刊写死规则
6. **文风贴合目标期刊**——整体写作风格以投稿期刊为基准校准：有样本论文时提取文风画像精调，无样本时按 profile 默认文风执行；范式卡管"骨架对不对"，文风画像管"读起来像不像这本刊"
7. **严禁编造文献**——只推荐"此处应引用什么类型的工作"，具体条目必须由用户提供或经检索确认

## 防呆规则

- 用户直接丢一段材料说"帮我写论文"→ 必须先引导完成 Step 0–1，不得直接产出正文
- 用户只要单章（如"帮我写 Introduction"）→ 可跳过完整流程，但必须先确认：目标期刊（选 profile）、该章在框架中的使命、输入材料形态；然后挂该章范式卡写作
- 用户已有英文初稿只要润色 → 从 Step 3 直接进入
- 论文内容用英文写；与用户的交互说明、质检报告用中文

## Step 0 初始化

**询问并确认四件事：**

1. **目标期刊/会议** → 套用 style profile（读 `references/profiles.md` 匹配；匹配不到则向用户确认关键参数后按最接近的 profile 执行）
   - ⚠️ **用户尚未确定投什么刊**（如问"投哪合适""Nature 子刊能不能投""帮我列候选期刊分梯队"）→ **先用 `期刊投稿选刊评估` 技能完成选刊，再回到本 Step 0 套 profile**。本技能假设期刊已选定，不做选刊评估。
2. **输入材料形态**（三入口）：
   - 入口 A：研究想法 + 实验数据 → 从零起稿
   - 入口 B：中文草稿 → 学术级翻译改写（非机翻：按范式卡重构，地道化学术表达）
   - 入口 C：英文初稿 → 润色升级（走 Step 3 质检 + 按需局部重写）
3. **论文类型**：Regular paper / Short paper / Letter / Methods article 等
4. **文风校准（强烈建议）**：请用户提供目标期刊近 2–3 年 2–3 篇代表性论文 PDF（用户欣赏的或主题相近的），从中提取**文风画像**：叙述节奏、论证密度、句式特征、修辞惯例、章节气质。无样本时按 profile 默认文风执行并告知用户是通用校准。文风画像写入框架契约。

## Step 1 框架规划（第一道确认关卡）

**核心任务：挑战点与创新点深挖 → 框架契约**

挑战点从三个维度扫描 SOTA 缺口：

| 维度 | 追问 | 产出 |
|------|------|------|
| 问题维度 | 现有方法没解决什么场景/约束？ | 未覆盖的问题空间 |
| 方法维度 | 现有方法的结构性缺陷是什么？ | 技术缺口分析 |
| 评估维度 | 现有实验设计有什么盲区？ | 评估缺口 |

每个缺口与用户方案/数据对照，形成 **"缺口 → 方案 → 证据"** 三段式论证链，确保创新点不是自说自话。

**产出：框架契约**——按 `references/contract-template.md` 模板生成（含：一句话定位、核心挑战、贡献列表、术语表、分章大纲（每章使命+章间衔接设计）、文风画像、文件命名清单）。保存为项目工作文件，后续每章强制回读。

**用户确认契约后才能进入 Step 2。**

## Step 2 分章写作（产出 Markdown）

**交互粒度分流：**

| 章节类型 | 交互模式 |
|----------|----------|
| Abstract / Introduction / Conclusion | 逐段共建：先出段落级论证方案（写什么、怎么论证），用户拍板后再落笔 |
| Related Work / Methodology / Experiments | 整章出稿，用户整体修改 |

**每章挂范式卡**（读 `references/paradigm-cards.md` 中对应章节）：结构骨架 + 时态规则 + 句式库 + 自查清单。三入口统一到同一范式卡质量标准。

**逻辑贯通机制（每章必做）：**
1. 动笔前回读框架契约（本章使命、衔接设计、术语表）
2. 完成后检查：开头是否兑现契约中的衔接设计；结尾是否按契约抛出下一章的问题
3. 术语一词到底；贡献表述与 Abstract 严格一致

**产出：Markdown 成稿**，图表占位符统一使用契约中"文件命名清单"的语义名（如 `【图 Figure2_architecture】`、`【表 table4_results_main】`），保证 LaTeX 化零歧义映射。

## Step 3 语言与规范质检（强制关卡）

按 `references/language-rules.md` 逐项执行：

1. **四条硬规则**（一票否决）：禁 em dash；禁无故造词（白名单放行公认术语）；标准学术词汇禁口语化（黑名单替换表）；去 AI 写作痕迹
2. **常规规范**：时态一致性、hedging 适度性、术语与缩写一致性、图表引用格式（按 profile）、引用密度
3. **文风一致性**：按文风画像逐章比对（节奏/句式/语态比例/贡献陈述方式/hedging 强度），发现"读起来像别的刊"的段落标注并改写

**产出：中文质检报告**（逐项问题 + 修改建议 + 修改后全文），经用户确认后定稿。

## Step 4 LaTeX 化（第二道确认关卡）

1. **交互确认官方模板**：文档类与样式文件（如 `neurips_2025.sty`、`ijcai26.sty` + `named.bst`、`IEEEtran.cls`、`sn-jnl.cls` 等），核对来源与版本
2. **按定稿工程结构生成 LaTeX 包**（结构如下，命名规则强制执行）：

```
paper/
├── main.tex                        # 骨架：documentclass + 宏包 + \input 按序引入各章
├── 0_abstract.tex                  # 每章一个独立 .tex，放包根目录
├── 1_introduction.tex
├── 2_relatedwork.tex
├── 3_methodology.tex
├── 4_results.tex
├── 6_conclusion.tex                # 编号留空位（5 可作 discussion），按实际结构取舍
├── 7_appendix.tex
├── image/                          # 图片单独存放
│   └── Figure{N}_{语义描述}.pdf    # N 与正文图号一致；禁止 1.png、fig_final_v2.pdf
├── table/                          # 一表一个 .tex 文件
│   └── table{N}_{所在章节}_{语义}.tex  # 如 table4_results_main.tex，看名即知位置与内容
├── reference.bib
└── {官方样式文件}.sty/.bst
```

3. **命名与引入规范：**
   - 章节文件：`{序号}_{章节名}.tex`，main.tex 用 `\input` 引入，main 不写正文
   - 表文件：完整 `\begin{table}...\end{table}` 环境，自带 `\caption` 与 `\label{tab:...}`，可独立预览；章节内 `\input{table/table4_results_main}` 引入
   - 图片：figure 环境中 `\includegraphics{image/Figure2_architecture.pdf}`
   - label 规范：图 `fig:{语义}`、表 `tab:{语义}`、公式 `eq:{语义}`、章节 `sec:{语义}`；禁用 `\ref{fig1}` 这类无语义 label

## Step 5 投稿支撑（按需触发）

按 `references/submission.md` 执行：
- **审稿人模拟**：方法学家 / 实验主义者 / 领域专家三视角评审，输出结构化 weaknesses（问题+严重度+预判审稿人措辞+应对建议）
- **Cover Letter**：为何适合该刊、创新点、无一稿多投声明
- **Rebuttal / Response to Reviewers**：逐条回应（感谢+直接回答+证据/修改位置），区分"完全照改/部分采纳并说明/礼貌反驳并论证"

## 贯穿全程：文献辅助

- **应引文献推荐**：提示"此处需支撑：XX 方向的代表性工作（类型）"——只给位置与类型，**不生成虚构条目**；条目须用户确认或经检索核实
- **BibTeX 辅助**：字段完整性检查、格式一致性、重复合并、key 命名规范
- **引用位置合理性**：标注"有论点无引用"或"引用堆砌"的段落

## 素材文件索引（按需加载，不要一次全读）

| 文件 | 何时读 |
|------|--------|
| `references/profiles.md` | Step 0 确定期刊后；质检核对结构规范与文风时 |
| `references/contract-template.md` | Step 1 生成框架契约时 |
| `references/paradigm-cards.md` | Step 2 写每章之前读该章范式卡 |
| `references/language-rules.md` | Step 3 质检时；任何产出英文段落前浏览硬规则 |
| `references/submission.md` | Step 5 投稿支撑时 |

## 已知边界（v1 不承诺，需向用户明示）

- 不直接联网检索文献入库（只推荐位置与类型）
- 不生成实验图表（只写 caption 与正文解读）
- 不做查重与 AI 检测器对抗（只做风格层面的去 AI 痕迹）
