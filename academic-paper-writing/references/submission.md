# 投稿支撑（Step 5，按需触发）

三个子功能：审稿人模拟、Cover Letter、Rebuttal / Response to Reviewers。

---

## 一、审稿人模拟（投稿前预判）

**三视角评审**，每个视角独立过一遍全文（回读框架契约作为评审基准）：

### 视角 1：方法学家（R1 挑技术）
- 理论严谨性：假设是否成立、推导是否完整、定理条件是否过强
- 形式化质量：问题定义是否清晰、目标函数是否合理
- 检查点：Methodology 逐公式过，找"没证明就断言"和"假设藏起来不声明"的段落

### 视角 2：实验主义者（R2 挑实验）
- 基线充分性：是否含近 2 年 SOTA、选型理由是否成立
- 消融完整性：贡献列表逐条是否有消融对应
- 对比公平性：调参预算是否对等、数据划分是否规范、统计显著性是否报告
- 检查点：Experiments 逐表过，找"只赢在有利指标"和"缺关键基线"的漏洞

### 视角 3：领域专家（R3 挑 novelty）
- novelty 是否成立：与最接近的 2–3 篇工作对比，差异是实质还是增量
- 定位是否诚实：claim 与证据范围是否匹配
- 适配性：内容是否真适合该刊 scope（还是投错了刊）

### 输出格式

```markdown
# 审稿人模拟报告（中文，供作者内部使用）
## 预判评分
R1(方法): x.x/10  R2(实验): x.x/10  R3(领域): x.x/10  综合: <borderline accept / reject 等>
## Weaknesses（按严重度排序）
### W1 <严重度：致命/重大/次要>
- 问题定位：<章节 + 段落>
- 预判审稿人措辞：<模拟审稿人原文，英文>
- 应对建议：<补实验 / 补证明 / 改措辞收窄 claim / 补引用>
## 建议的投稿前修改清单
（按性价比排序：先做能显著提升得分的）
```

---

## 二、Cover Letter

**结构**（一页以内，英文）：

1. 抬头：Dear Editor-in-Chief / Dear Editors
2. 投稿声明：On behalf of all co-authors, I am submitting our manuscript entitled "[Title]" (Article Type) for consideration in [Journal].
3. 一句话核心内容：The manuscript addresses ... by ...
4. 创新点 2–3 条：与框架契约贡献列表同源，换投稿导向措辞（强调对期刊读者群的价值）
5. 适配性声明：为什么适合该刊 scope 与读者（一句到两句，具体）
6. 声明：original work, not under consideration elsewhere, all authors approved
7. （可选）建议/回避审稿人：按期刊政策，给 name + affiliation + 理由
8. 落款：Corresponding author 信息

**自查**：不复制 Abstract；语气专业不谄媚；无未在正文兑现的 claim。

---

## 三、Rebuttal / Response to Reviewers

**总原则**：逐条回应、绝不遗漏、态度专业；每条回应让审稿人看到"被认真对待"，而非"被应付"。

### 逐条回应结构

```latex
\textbf{Reviewer #N, Comment #M:} \textit{<原文摘录>}

\textbf{Response:} We thank the reviewer for ...
<直接回答>
<Evidence: 新实验数据/证明，或修改位置 "Section X, Page Y, Lines Z">
<修改原文摘录（如适用）>
```

### 三种应对策略（先分类再动笔）

| 审稿意见类型 | 策略 | 写法要点 |
|--------------|------|----------|
| 合理且可改 | 完全照改 | 感谢 + 直接改 + 标注修改位置；能改的别嘴硬 |
| 部分合理 | 部分采纳并说明 | 先肯定合理部分并修改；对不合理部分用证据礼貌说明，不攻击审稿人 |
| 基于误读或不可行 | 礼貌反驳并论证 | 先澄清误解（"We apologize for the unclear presentation..."，把责任揽到表述不清上）；再给证据/新实验；绝不写"the reviewer is wrong" |

### 高危信号处理

- **novelty 质疑**：补与所指工作的逐点对比表，写实质差异；必要时补实验
- **缺基线**：能补则补（rebuttal 期新增实验是加分项）；补不了则说明原因 + 承诺 camera-ready 补
- **统计性不足**：补误差棒/多 seed/p-value，这是最容易被安抚的意见
- **over-claim**：主动收窄措辞，改 claim 比争论划算

### 格式惯例

- 开头总回应段（Response to all reviewers）：感谢 + 概括主要修改
- 每条编号回应，与审稿意见一一对应
- 修改位置精确到 Section / Page / Line
- 长度克制：单条回应 ≤ 一屏，重证据轻情绪
- 全文通过 Step 3 硬规则质检（禁 em dash 等，同样适用于 rebuttal）
