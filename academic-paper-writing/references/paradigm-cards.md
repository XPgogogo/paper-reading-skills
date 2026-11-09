# 范式卡（分章写作核心资产）

每章一张卡，四要素：**结构骨架 + 时态规则 + 句式库 + 自查清单**。
三入口（从零起稿 / 中文改写 / 英文润色）统一到同一范式卡质量标准。
写作前另需回读框架契约：本章使命、衔接设计、术语表、文风画像。

---

## Abstract

**结构骨架**（150–250 词，按 profile 调整）：
1. 背景 1–2 句：领域 + 任务，不写教科书式铺垫
2. Gap 1 句：现有方法的关键缺口（与 Intro 的 gap 同源）
3. 方法 2–3 句：本文方案，第一个动词就亮出核心技术
4. 结果与意义 2–3 句：关键数字 + 一句意义升华

**时态规则**：背景/领域事实用现在时；本文做了什么用现在时（this paper presents...）；结果用现在时或过去时保持一致。

**句式库**：
- 开头：`X has emerged as a fundamental challenge in ...` / `Recent advances in X have enabled ..., yet ...`
- Gap：`However, existing approaches suffer from ...` / `... remains largely unexplored.`
- 方法：`In this paper, we propose [Name], a ... that ...` / `We introduce ...`
- 结果：`Extensive experiments on X demonstrate that [Name] outperforms ... by ...` / `achieves a ... improvement over ...`

**自查清单**：
- [ ] 无引用、无编号引用、缩写慎用（只保留领域公认缩写）
- [ ] 至少一个量化数字亮点
- [ ] 贡献表述与 Introduction 的贡献列表严格一致（数量与措辞对应）
- [ ] 与 Conclusion 不矛盾

---

## Introduction（逐段共建章节）

**结构骨架**（漏斗五段）：
1. 领域宏观：任务重要性，1–2 句到位，不写百科
2. 具体问题：聚焦到本文解决的那个问题
3. 现有方法脉络：按流派归类（非流水账），每派一句话概括思路
4. Gap 分析：现有方法的共同缺陷，每个 gap 有引用或实验证据支撑；从框架契约的"缺口→方案→证据"论证链取材
5. 贡献列表 + 全文组织：bullet 式（P1）或行文式（P2/P4），每条贡献对应一个实验/理论支撑

**时态规则**：领域事实现在时；前人工作现在时/现在完成时（has explored）；本文工作现在时。

**句式库**：
- 流派概括：`Existing methods can be broadly categorized into ...` / `Prior efforts fall into two lines: ...`
- Gap：`Despite this progress, a critical limitation persists: ...` / `However, these methods overlook ...`
- 贡献：`Our main contributions are summarized as follows:` / `This paper makes three contributions:`
- 组织段：`The remainder of this paper is organized as follows.`（P2 常用；P1/P4 可省略）

**自查清单**：
- [ ] 漏斗每段比上一段更聚焦，段间有过渡
- [ ] 每个 gap 有文献或数据支撑，非自说自话
- [ ] 贡献条数与 Abstract、框架契约一致
- [ ] 结尾按契约抛出 Methodology 要接的问题
- [ ] 篇幅符合 profile（P1 一页内见方法，P2 可 1.5–2 页）

---

## Related Work

**结构骨架**：
1. 开头 1–2 句：综述组织方式的预告（按方法流派或问题维度）
2. 分类综述：每类 = 概括思路 + 代表工作 + 一句优劣点评（批判性，非描述性）
3. 对比表格（可选，但强烈建议）：table1_relatedwork_comparison
4. 结尾定位：本文与各流派的关系，凸显差异而非重复

**时态规则**：介绍前人工作用过去时（proposed, introduced）或现在完成时；评述其性质用现在时（this approach relies on ...）。

**句式库**：
- 分类：`Research on X can be broadly grouped into three categories: ...`
- 点评优势：`This line of work effectively addresses ...`
- 点评局限：`Nevertheless, these methods are constrained by ...` / `In contrast to ..., our approach ...`
- 定位：`Unlike prior studies that ..., we ...` / `Our work is orthogonal to ... and complements ...`

**自查清单**：
- [ ] 每类结尾有批判性点评，引出本文差异
- [ ] 无流水账（连续 "A did X. B did Y. C did Z."）
- [ ] 覆盖近 2–3 年 SOTA，无严重遗漏
- [ ] 与 Introduction 的 gap 分析呼应、不重复相同句子
- [ ] 结尾定位段直接为 Methodology 铺路

---

## Methodology

**结构骨架**：
1. Overview：开头段 + 全方法总览图（Figure1/Figure2_overview）
2. 符号系统：Notation 小节或表格（table{N}_methodology_symbols），全文符号一表到底
3. 问题形式化：假设与优化目标的数学定义
4. 方法分模块展开：每个模块一小节，"动机句 → 形式化 → 算法/流程"
5. 复杂度/理论分析（P2 必备，P1 可后移附录）

**时态规则**：描述本文方法一律现在时（our model first encodes ...）；不写 we will，直接写事实。

**句式库**：
- 动机句：`To capture ..., we design ...` / `A key challenge here is ...; to address it, we ...`
- 公式引入：`Formally, given ..., we define ... as` / `The objective is formulated as:`
- 公式叙述：`where X denotes ..., Y is the ..., and Z represents ...`（where 从句规范）
- 模块衔接：`Building upon the obtained ..., we further ...`
- 设计决策：`The rationale behind this design is twofold: ...`

**自查清单**：
- [ ] 每个符号在符号表或首现处定义，无未定义符号
- [ ] 每个设计决策带动机句（不堆砌技术）
- [ ] 公式编号与正文引用（\eqref）对齐
- [ ] 与框架契约的贡献列表逐条可追溯（每个贡献在此有对应模块）
- [ ] 结尾抛出"该方法是否有效"的实证问题，衔接 Experiments

---

## Experiments / Results

**结构骨架**：
1. Setup：数据集（来源+规模+划分）、基线（选型理由）、评价指标、实现细节（复现关键参数）
2. 主实验：与 SOTA 全面对比（table{N}_results_main），不止报数，要有解读
3. 消融实验（table{N}_results_ablation）：逐个拆解设计决策的贡献
4. 分析实验：参数敏感性、案例研究、可视化（P1/P3 常见）

**时态规则**：描述实验设置与过程用过去时（we conducted, was trained）；报告图表内容用现在时（Table 2 shows that ...）；解读发现用现在时。

**句式库**：
- 图表引入：`Table 2 reports the ...` / `As shown in Figure 3, ...`
- 解读（关键句式）：`We attribute this improvement to ...` / `This is because ...` / `A plausible explanation is that ...`
- 消融：`Removing component X degrades performance by ..., confirming its contribution to ...`
- 对比：`[Name] consistently outperforms ... across all datasets` / `notably, ...`

**自查清单**：
- [ ] 每个图表必被正文引用，且引用后必跟解读（忌只描述不解释）
- [ ] 每个数字结论与统计显著性/重复次数说明（P3 必查）
- [ ] 消融覆盖框架契约中的全部贡献点
- [ ] 基线选型有一句话理由，包含近 2 年 SOTA
- [ ] 实验设置信息足以复现（P3 硬要求）

---

## Conclusion（逐段共建章节）

**结构骨架**（1–2 段）：
1. 贡献回顾：换措辞重述核心贡献与关键结果（不复制 Abstract）
2. 局限：诚实点出 1–2 条（给审稿人留好台阶）
3. 展望：1–2 句未来方向（具体，不喊口号）

**时态规则**：总结本文用现在时/现在完成时；展望用将来时或 will/plan to。

**句式库**：
- 开头：`In this paper, we presented [Name], a ... for ...` / `This paper introduced ...`
- 结果回收：`Extensive experiments demonstrate that ...`（措辞与 Abstract 区分）
- 局限：`One limitation of our approach is ...; extending ... is left as future work.`
- 展望：`A promising direction is to ...` / `In future work, we plan to ...`

**自查清单**：
- [ ] 不引入任何新信息、新引用、新实验
- [ ] 局限表述诚实且不自我贬损
- [ ] 与 Abstract 的贡献表述一致但措辞不同
- [ ] 篇幅克制（P4 尤甚）

---

## Appendix（如 profile 需要）

- 放证明、额外实验、实现细节、复现清单
- 正文提及时必须给出附录指引（see Appendix A.2）
- P1 profile：正文 8 页限制下，可把次要实验全部后移，正文只留主线
