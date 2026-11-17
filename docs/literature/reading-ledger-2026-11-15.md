# Literature reading ledger (biology, 2026-11-15)

**Scope:** 131 deduplicated scholarly records; 102 have abstract/selected-section/proof reading evidence. **Reading a paper abstract does not mean a full-text reading.** Items marked `bibliography_verified` were checked bibliographically only. This file transcribes individual records and notes from the 2026-11-15 research audit, rather than implying independent external peer review. Scholarly chapters/lecture notes are included where they are mathematical tools. No exhaustive literature novelty or authorship priority is claimed.

Reading status legend: `bibliography_verified` = metadata only; `abstract_read` = abstract; `fulltext_sections_read` = selected full-text sections; `proof_audited` = specified claim/proof audited. Review and re-check any priority claim against publisher versions and later citing work.

### BIO001 · 2019 — On logical bifurcation diagrams

- **Author / form:** Abou-Jaoudé W; Monteiro PT · journal_paper
- **Theme / reading status:** `GRN_multistability` / `abstract_read`
- **Source:** https://doi.org/10.1016/j.jtbi.2019.01.008
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 把逻辑参数变化与一族分段线性微分模型相联系；Boolean 情况用偏序刻画可实现的逻辑分岔序列，并构造最长序列。对本仓库的作用是区分‘均匀抽取规则’与‘沿可实现参数路径改变规则’；摘要没有给出任意两规则间的生物参数插值保证。

### BIO002 · 2026 — Characterization of monotone Boolean models supporting fixed points and multistability in balanced networks

- **Author / form:** Sarah Adigwe; B. V. Harshavardhan; Mohit Kumar Jolly; Tomáš Gedeon · journal_paper
- **Theme / reading status:** `GRN_multistability` / `fulltext_sections_read`
- **Source:** https://doi.org/10.1371/journal.pcsy.0000103
- **Actually inspected:** Abstract；Introduction；Lattice and equilibrium-support construction；Discussion
- **Specific takeaway / limitation:** 已读摘要、引言、格与平衡态集合的主要构造、讨论。平衡符号网络可通过变量补变换联系到全正网络；支持某状态的模型集合用单调函数格中的理想/滤子及其乘积表达，导出规定模型测度中的流行度关系。边可冗余，实际影响图可为给定图的子图。讨论指出任意符号网络、一般吸引子与 DSGRN 联系仍需研究。该测度的流行度不是经过校准的细胞占据概率。自动元数据检索曾返回配套 Zenodo 代码集，已人工替换为正文 DOI，代码集不计入论文数量。

### BIO003 · 2022 — Emergence of dynamic properties in network hypermotifs

- **Author / form:** Adler M; Medzhitov R · journal_paper
- **Theme / reading status:** `GRN_multistability` / `abstract_read`
- **Source:** https://doi.org/10.1073/pnas.2204967119
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 将网络模体作为高一层的节点，研究模体如何组合以及组合后出现的动力学性质。结果依赖具体组合结构，提示当前仅按每节点抑制入度计数的乘积目标无法检验这类中尺度机制；不能据本文摘要断言某一超模体普遍最优。

### BIO004 · 2025 — Emergent dynamics of cellular decision making in multi-node mutually repressive regulatory networks

- **Author / form:** Bv H; Billakurthi HS; Adigwe S; Hari K; Levine H; Gedeon T; Jolly MK · journal_paper
- **Theme / reading status:** `GRN_multistability` / `abstract_read`
- **Source:** https://doi.org/10.1098/rsif.2025.0190
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 研究 toggle-n 的互相抑制架构，结合数值与解析方法发现多个主调控因子共表达的混合表型；细胞因子信号和边强度不对称可推动进一步分化。其状态集合与本仓库同时要求全部 single-high 固定点不同，不能将两种目标的‘最优架构’直接等同。

### BIO005 · 2026 — UNified FramewOrk for reguLatory Dynamics (UNFOLD): Dissecting robustness, plasticity, evolvability and canalisation of biological function

- **Author / form:** Chakraborty D; Rengaswamy R; Raman K · journal_paper
- **Theme / reading status:** `GRN_multistability` / `abstract_read`
- **Source:** https://doi.org/10.1371/journal.pcbi.1014289
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 在所扫描参数域内对全部三基因拓扑的大规模动力学模拟按响应形状分类，提出结构、参数、功能多样性指标。20 类功能和各比例是该扫描与分类设定内的结果，并非任意维数、任意参数的分类定理。

### BIO006 · 2019 — Synthesis of Boolean Networks from Biological Dynamical Constraints using Answer-Set Programming

- **Author / form:** Stéphanie Chevalier; Christine Froidevaux; Loïc Paulevé; Andrei Y. Zinovyev · conference_paper
- **Theme / reading status:** `GRN_multistability` / `abstract_read`
- **Source:** https://doi.org/10.1109/ictai.2019.00014
- **Actually inspected:** Abstract (complete, indexed metadata)
- **Specific takeaway / limitation:** 把部分观测状态之间的可达性、固定点及吸引子约束编码为 ASP，完整且不重复地刻画满足约束的 Boolean 模型。适合作为非单独固定点约束的新模型生成与独立验证工具；其规模表现随约束类型而变。

### BIO007 · 2016 — Combinatorial representation of parameter space for switching networks

- **Author / form:** Cummins B; Gedeon T; Harker S; Mischaikow K; Mok K · journal_paper
- **Theme / reading status:** `GRN_multistability` / `abstract_read`
- **Source:** https://doi.org/10.1137/15m1052743
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** DSGRN 将切换系统的参数空间有限分割，使每块的带注释 Morse 图不变。它处理的是给定调控图的参数化动力学，而不只是固定点存在性；可用于检验 Boolean 规则均匀计数是否符合更细的参数几何。

### BIO008 · 2026 — Boolean models coarsely sample continuous dynamics of regulatory networks

- **Author / form:** Cummins, Breschine; Gameiro, Marcio; Gedeon, Tomáš; Mischaikow, Konstantin; Rivas, Bernardo · journal_paper
- **Theme / reading status:** `GRN_multistability` / `fulltext_sections_read`
- **Source:** https://doi.org/10.48550/arxiv.2606.14925
- **Actually inspected:** Abstract；Introduction；Section 3.11 definitions；Lemma 3.42 and Theorem 3.43 including proofs；Conclusion
- **Specific takeaway / limitation:** 已读摘要、引言、§3.11 的定义及 Lemma 3.42/Theorem 3.43 全部证明、结论。论文把每节点 Boolean 规则复制为对应多值参数链，构造节点相关的单调 binarization，并证明生成的多值更新是 trivial multilevel refinement。证明利用 g_i 仅取 0 或最大层级的结构，不能推成所有多值参数都与原 Boolean 模型等价。例子显示 Boolean 模型可能漏掉中间多稳态和周期轨道。因此未来若声称生物‘最优结构’，须说明是在 Boolean 子族、DSGRN 参数块还是连续参数测度中优化。

### BIO009 · 2015 — A Modelling Framework for Gene Regulatory Networks Including Transcription and Translation

- **Author / form:** Edwards R; Machina A; McGregor G; van den Driessche P · journal_paper
- **Theme / reading status:** `GRN_multistability` / `abstract_read`
- **Source:** https://doi.org/10.1007/s11538-015-0073-9
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 显式加入 mRNA 与蛋白变量。任一类变量无限快时可在任意有限时间区间一致逼近简化模型，但文章给出简化模型稳定固定点在扩展模型中失稳的例子。有限时间逼近不自动保护长期吸引子，是模型推广时必须保留的限定。

### BIO010 · 2001 — Chaos in neural and gene networks with hard switching

- **Author / form:** Edwards R · journal_paper
- **Theme / reading status:** `GRN_multistability` / `bibliography_verified`
- **Source:** https://link.springer.com/article/10.1007/s11538-026-01791-4
- **Actually inspected:** Not recorded beyond bibliography
- **Specific takeaway / limitation:** 仅核验作者、题名、年份及论文引用；未读原文摘要或正文，未从题名推断结论。

### BIO011 · 2000 — Construction of a genetic toggle switch in Escherichia coli

- **Author / form:** Gardner TS; Cantor CR; Collins JJ · journal_paper
- **Theme / reading status:** `GRN_multistability` / `abstract_read`
- **Source:** https://doi.org/10.1038/35002131
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 实验构建互相抑制的两基因开关并给出双稳态条件，是 toggle-switch 生物动机的直接依据。两节点实验及其参数化理论不意味着完全抑制网络在更大 n 下具有最高规则计数。

### BIO012 · 2020 — Multi-parameter exploration of dynamics of regulatory networks

- **Author / form:** Gedeon T · journal_paper
- **Theme / reading status:** `GRN_multistability` / `abstract_read`
- **Source:** https://doi.org/10.1016/j.biosystems.2020.104113
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 综述结合微分方程与 Boolean 逻辑的组合参数化方法，可在可计算规模内跨参数比较网络动力学。所讨论问题来源于生物参数不确定性；离散参数块数量仍不等于实验中参数的概率分布。

### BIO013 · 2024 — Lattice structures that parameterize regulatory network dynamics

- **Author / form:** Gedeon T · journal_paper
- **Theme / reading status:** `GRN_multistability` / `abstract_read`
- **Source:** https://doi.org/10.1016/j.mbs.2024.109225
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 构造单调 Boolean 函数格、非退化函数偏序及链格的归纳表示，分别用于 Boolean 与切换 ODE 模型。摘要明确指出 Dedekind 数规模限制；这是本仓库枚举表示的理论基础，而不是对 n>5 极值结构的现成答案。

### BIO014 · 2024 — Network topology and interaction logic determine states it supports

- **Author / form:** Gedeon T · journal_paper
- **Theme / reading status:** `GRN_multistability` / `abstract_read`
- **Source:** https://doi.org/10.1038/s41540-024-00423-8
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 综述多值单调逻辑与 ODE 模型的联系，并用模型集合研究平衡态的支持与流行度。适合校准‘支持某表型’这一术语，但仅据摘要无法推出不同连续参数先验下的概率不变性。

### BIO015 · 2014 — Multistable switches and their role in cellular differentiation networks

- **Author / form:** Ghaffarizadeh A; Flann NS; Podgorski GJ · journal_paper
- **Theme / reading status:** `GRN_multistability` / `abstract_read`
- **Source:** https://doi.org/10.1186/1471-2105-15-s7-s7
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 在分化模型和随机 Boolean 网络中嵌入多稳态开关，研究吸引子间的分离与跃迁方向性；重复开关的效应比单个明显。研究量已经涉及转换障碍，说明仅计数固定点不能覆盖分化稳定性的全部问题。

### BIO016 · 1973 — The logical analysis of continuous, non-linear biochemical control networks

- **Author / form:** Glass L; Kauffman SA · journal_paper
- **Theme / reading status:** `GRN_multistability` / `bibliography_verified`
- **Source:** https://doi.org/10.1016/0022-5193(73)90208-7
- **Actually inspected:** Not recorded beyond bibliography
- **Specific takeaway / limitation:** 仅核验作者、题名、年份及论文引用；未读原文摘要或正文，未从题名推断结论。

### BIO017 · 2023 — A computation of the ninth Dedekind number

- **Author / form:** Jäkel, Christian · journal_paper
- **Theme / reading status:** `GRN_multistability` / `abstract_read`
- **Source:** https://doi.org/10.1016/j.jaca.2023.100006
- **Actually inspected:** Abstract (complete, arXiv)
- **Specific takeaway / limitation:** 通过矩阵运算与自由分配格对称性计算第九 Dedekind 数。其意义是提供计数方法和校验素材；我们不把已知 D(9) 的大整数计算当作解释 GRN 极值转移的替代品。

### BIO018 · 2026 — Gene regulatory networks: from correlative models to causal explanations

- **Author / form:** Maizels RJ; Briscoe J · journal_paper
- **Theme / reading status:** `GRN_multistability` / `abstract_read`
- **Source:** https://doi.org/10.1038/s41576-026-00939-1
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 提出从相关性网络转向机制性解释的研究框架，强调生物约束、机制模型及扰动实验。它支持以可反驳动力学命题选择数学问题，但本身属于综述与研究主张，不是本仓库的极值定理。

### BIO019 · 2017 — Assessing regulatory information in developmental gene regulatory networks

- **Author / form:** Peter IS; Davidson EH · journal_paper
- **Theme / reading status:** `GRN_multistability` / `abstract_read`
- **Source:** https://doi.org/10.1073/pnas.1610616114
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 结合已知发育调控子回路、Boolean 模型与扰动，分析节点逻辑、子回路和层级网络如何整合调控信息。用作表型编码和结构约束的背景，不能从局部 motif 推出全网通用定理。

### BIO020 · 2020 — Benchmarking algorithms for gene regulatory network inference from single-cell transcriptomic data

- **Author / form:** Pratapa A; Jalihal AP; Law JN; Bharadwaj A; Murali TM · journal_paper
- **Theme / reading status:** `GRN_multistability` / `abstract_read`
- **Source:** https://doi.org/10.1038/s41592-019-0690-6
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** BEELINE 对单细胞 GRN 推断进行有真值的基准比较；综合指标并不理想，模拟网络较实证 Boolean 模型更易恢复。这提醒未来以推断网络验证数学定理时需显式建模边符号与拓扑的不确定性。

### BIO021 · 2025 — Operating principles of interconnected feedback loops driving cell fate transitions

- **Author / form:** Rashid M; Hegade A · journal_paper
- **Theme / reading status:** `GRN_multistability` / `abstract_read`
- **Source:** https://doi.org/10.1038/s41540-024-00483-w
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 比较反馈环数量相同而拓扑不同的网络，并观察自调控对稳态分布的影响。这种结构依赖性与本仓库同入度序列严格同计数的性质不同，适合作为选择新目标函数的对照。

### BIO022 · 2023 — Robustness and innovation in synthetic genotype networks

- **Author / form:** Santos-Moreno J; Tasiudi E; Kusumawardhani H; Stelling J; Schaerli Y · journal_paper
- **Theme / reading status:** `GRN_multistability` / `abstract_read`
- **Source:** https://doi.org/10.1038/s41467-023-38033-3
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 实验构建三节点 CRISPRi 调控网络的互相连接基因型网络，结合建模刻画鲁棒性与可进化性。这里的邻接由具体突变决定；当前规则集合中的单点翻转是否对应这种可实现突变需要另证。

### BIO023 · 2026 — Network hypermotifs in biological systems: structure, dynamics, and functional implications

- **Author / form:** Singh MS; Bhattacharya P; Raman K · journal_paper
- **Theme / reading status:** `GRN_multistability` / `abstract_read`
- **Source:** https://doi.org/10.1038/s41540-026-00701-7
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 综述由多个网络模体组合而成的高阶结构及其动力学功能。用于定位中尺度问题；本次只读摘要，不据此提出未经原文验证的具体数学猜想。

### BIO024 · 2006 — Stochastic models for regulatory networks of the genetic toggle switch

- **Author / form:** Tian T; Burrage K · journal_paper
- **Theme / reading status:** `GRN_multistability` / `abstract_read`
- **Source:** https://doi.org/10.1073/pnas.0507818103
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 在 ODE 基础上引入 Poisson 随机变量，构造开关的随机模型以重现群体双峰分布。随机切换概率和确定性多稳态存在性不同，提示不要把规则数比例解读为细胞占据率。

### BIO025 · 2019 — An enriched network motif family regulates multistep cell fate transitions with restricted reversibility

- **Author / form:** Ye Y; Kang X; Bailey J; Li C; Hong T · journal_paper
- **Theme / reading status:** `GRN_multistability` / `abstract_read`
- **Source:** https://doi.org/10.1371/journal.pcbi.1006855
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 搜索可产生四个逐步变化吸引子的模体家族，并在 T 细胞模型中计算景观与最小作用路径。可逆性与跃迁路径是比固定点数量更丰富的约束；文中结构家族是该建模设定中的发现。

### BIO026 · 2021 — A comprehensive overview and critical evaluation of gene regulatory network inference technologies

- **Author / form:** Zhao M; He W; Tang J; Zou Q; Guo F · journal_paper
- **Theme / reading status:** `GRN_multistability` / `abstract_read`
- **Source:** https://doi.org/10.1093/bib/bbab009
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 评述并比较模型型、信息型与机器学习型 GRN 重建技术，强调不同假设与网络规模对结果的影响。它是数据验证方案的背景文献，不是 Boolean 极值计数的证明工具。

### BIO027 · 2011 — Understanding gene circuits at cell-fate branch points for rational cell reprogramming

- **Author / form:** Zhou JX; Huang S · journal_paper
- **Theme / reading status:** `GRN_multistability` / `abstract_read`
- **Source:** https://doi.org/10.1016/j.tig.2010.11.002
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 综述交叉抑制和自激活在分化分叉点的作用，并主张通过动力学景观理解重编程。提供单高表型问题的生物动机，同时提醒其仅是一类细胞命运编码。

### BIO028 · 2016 — Relative stability of network states in Boolean network models of gene regulation in development

- **Author / form:** Zhou JX; Samal A; d&#x27;Hérouël AF; Price ND; Huang S · journal_paper
- **Theme / reading status:** `GRN_multistability` / `abstract_read`
- **Source:** https://doi.org/10.1016/j.biosystems.2016.03.002
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 为离散 Boolean 网络定义相对稳定性景观，在胰腺分化模型中联合使用结构、固定点和相对稳定性排序约束。该排序约束排除了单靠固定点存在性不能区分的规则，是可直接移植的目标修正思路。

### BIO029 · 2022 — Synthetic multistability in mammalian cells

- **Author / form:** Zhu R; Del Rio-Salgado JM; Garcia-Ojalvo J; Elowitz MB · journal_paper
- **Theme / reading status:** `GRN_multistability` / `abstract_read`
- **Source:** https://doi.org/10.1126/science.abg9765
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** MultiFate 以自激活和互相抑制构建可控制的哺乳动物多稳态电路，报告长期保持多个状态与外部输入切换。实验显示多种高表达组合具有意义，故‘全部 single-high’不能默认代表全部多命运功能。

### BIO030 · 2015 — An Ovol2-Zeb1 Mutual Inhibitory Circuit Governs Bidirectional and Multi-step Transition between Epithelial and Mesenchymal States

- **Author / form:** Hong T; Watanabe K; Ta CH; Villarreal-Ponce A; Nie Q; Dai X · journal_paper
- **Theme / reading status:** `GRN_structure_and_dynamics` / `abstract_read`
- **Source:** https://doi.org/10.1371/journal.pcbi.1004569
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 结合实验与建模，Ovol2–Zeb1 互抑制产生含两个中间表型的四态系统，并影响双向转变。用来检验单高固定点假设的适用范围，不将病理机制推断为本仓库的生物结论。

### BIO031 · 2017 — Interrogating the topological robustness of gene regulatory circuits by randomization

- **Author / form:** Huang B; Lu M; Jia D; Ben-Jacob E; Levine H; Onuchic JN · journal_paper
- **Theme / reading status:** `GRN_structure_and_dynamics` / `abstract_read`
- **Source:** https://doi.org/10.1371/journal.pcbi.1005456
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** RACIPE 对固定拓扑随机化动力学参数并汇总稳态，发现表型聚类的鲁棒性。统计结论依赖参数抽样方案；需与单调 Boolean 规则均匀测度区别处理。

### BIO032 · 2015 — A Boolean network model of human gonadal sex determination

- **Author / form:** Ríos O; Frias S; Rodríguez A; Kofman S; Merchant H; Torres L; Mendoza L · journal_paper
- **Theme / reading status:** `GRN_structure_and_dynamics` / `abstract_read`
- **Source:** https://doi.org/10.1186/s12976-015-0023-0
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 对人类性腺分化网络构建同步 Boolean 模型，在野生型与突变条件下得到有生物解释的吸引子。同步更新是结果解释的一部分，不能把其非固定点吸引子移植到异步模型。

### BIO033 · 2011 — Systematic search for recipes to generate induced pluripotent stem cells

- **Author / form:** Chang R; Shoemaker R; Wang W · journal_paper
- **Theme / reading status:** `GRN_structure_and_dynamics` / `abstract_read`
- **Source:** https://doi.org/10.1371/journal.pcbi.1002300
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 通过系统生物学模型搜索诱导多能干细胞配方，并追踪重编程状态和景观。作为应用背景，它表明可控制可达性比单独增加候选规则数更接近干预任务；本次只读摘要。

### BIO034 · 2017 — Novel Hybrid Phenotype Revealed in Small Cell Lung Cancer by a Transcription Factor Network Model That Can Explain Tumor Heterogeneity

- **Author / form:** Udyavar AR; Wooten DJ; Hoeksema M; Bansal M; Califano A; Estrada L; Schnell S; Irish JM; Massion PP; Quaranta V · journal_paper
- **Theme / reading status:** `GRN_structure_and_dynamics` / `abstract_read`
- **Source:** https://doi.org/10.1158/0008-5472.can-16-1467
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** Boolean 转录因子网络预测 SCLC 混合表型，随后用细胞与肿瘤样本验证相关标记。该案例支持以预测与实验检验连接模型；它不为任意 signed graph 的均匀规则计数提供先验依据。

### BIO035 · 2008 — Functional organisation of Escherichia coli transcriptional regulatory network

- **Author / form:** Martínez-Antonio A; Janga SC; Thieffry D · journal_paper
- **Theme / reading status:** `GRN_structure_and_dynamics` / `abstract_read`
- **Source:** https://doi.org/10.1016/j.jmb.2008.05.054
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** E. coli 网络中不同功能子网具有不同反馈和路径分布，正自调控较多见于发育相关过程，代谢调控有其他模式。当前全正自环假设应作为选定模型范围，不能普遍外推到所有 GRN。

### BIO036 · 2008 — Network model of survival signaling in large granular lymphocyte leukemia

- **Author / form:** Zhang R; Shah MV; Yang J; Nyland SB; Liu X; Yun JK; Albert R; Loughran TP Jr · journal_paper
- **Theme / reading status:** `GRN_structure_and_dynamics` / `abstract_read`
- **Source:** https://doi.org/10.1073/pnas.0806447105
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 将文献中的 T-LGL 生存信号汇入离散模型，提出并实验验证若干干预预测。说明生物价值依赖具体可检验的输出；本次仅阅读摘要，不重述或外推临床治疗建议。

### BIO037 · 2016 — Logical Modeling and Dynamical Analysis of Cellular Networks

- **Author / form:** Abou-Jaoudé W; Traynard P; Monteiro PT; Saez-Rodriguez J; Helikar T; Thieffry D; Chaouiya C · journal_paper
- **Theme / reading status:** `GRN_structure_and_dynamics` / `abstract_read`
- **Source:** https://doi.org/10.3389/fgene.2016.00094
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 综述逻辑模型的吸引子、可达性、外部信号变化与模型缩减方法，并以 T 细胞分化和细胞周期示例。它帮助界定研究层次；仅有固定点定理不等于完整动态行为分类。

### BIO038 · 2018 — RACIPE: a computational tool for modeling gene regulatory circuits using randomization

- **Author / form:** Huang B; Jia D; Feng J; Levine H; Onuchic JN; Lu M · journal_paper
- **Theme / reading status:** `GRN_structure_and_dynamics` / `abstract_read`
- **Source:** https://doi.org/10.1186/s12918-018-0594-6
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 介绍 RACIPE 实现及参数随机化后的统计分析，用于耦合开关等网络。参数无精确测量不表示没有抽样假设；均匀抽规则与随机化 ODE 的分布需要单独比较。

### BIO039 · 2018 — Topography of epithelial-mesenchymal plasticity

- **Author / form:** Font-Clos F; Zapperi S; La Porta CAM · journal_paper
- **Theme / reading status:** `GRN_structure_and_dynamics` / `abstract_read`
- **Source:** https://doi.org/10.1073/pnas.1722609115
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 用 Boolean 模型及转录数据构建 EMT 表型地形，发现多个混合亚稳态。‘亚稳态’与严格固定点不同，为后续带噪声或跃迁约束的建模提供参照。

### BIO040 · 2012 — Logical modelling of gene regulatory networks with GINsim

- **Author / form:** Chaouiya C; Naldi A; Thieffry D · methods_book_chapter
- **Theme / reading status:** `GRN_structure_and_dynamics` / `abstract_read`
- **Source:** https://doi.org/10.1007/978-1-61779-361-5_23
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 以噬菌体 λ 为例介绍 GINsim 的逻辑建模与分析流程。作为方法章节支持复现与更新语义核查；没有从该摘要提取开放定理。

### BIO041 · 2017 — MaBoSS 2.0: an environment for stochastic Boolean modeling

- **Author / form:** Stoll G; Caron B; Viara E; Dugourd A; Zinovyev A; Naldi A; Kroemer G; Barillot E; Calzone L · journal_paper
- **Theme / reading status:** `GRN_structure_and_dynamics` / `abstract_read`
- **Source:** https://doi.org/10.1093/bioinformatics/btx123
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** MaBoSS 以随机 Boolean 动力学输出随时间变化的概率，并支持突变和敏感性分析。它可以测试新的动态研究量，但模拟结果依赖转移速率，无法自动替代解析普适结论。

### BIO042 · 2014 — Boolean modeling: a logic-based dynamic approach for understanding signaling and regulatory networks and for making useful predictions

- **Author / form:** Albert R; Thakar J · journal_paper
- **Theme / reading status:** `GRN_structure_and_dynamics` / `abstract_read`
- **Source:** https://doi.org/10.1002/wsbm.1273
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 介绍 Boolean 模型如何以阈值和逻辑规则表达调控、提取稳定模式并引导实验。其‘无参数’描述指不需连续动力学速率；规则选择本身仍携带建模假设。

### BIO043 · 2003 — Monotone Boolean functions

- **Author / form:** A D Korshunov · journal_paper
- **Theme / reading status:** `GRN_structure_and_dynamics` / `bibliography_verified`
- **Source:** https://doi.org/10.1070/rm2003v058n05abeh000667
- **Actually inspected:** Not recorded beyond bibliography
- **Specific takeaway / limitation:** 仅核验作者、题名、年份及论文引用；未读原文摘要或正文，未从题名推断结论。

### BIO044 · 2001 — Algorithms counting monotone Boolean functions

- **Author / form:** Robert Fidytek; Andrzej W. Mostowski; Rafał Somla; Andrzej Szepietowski · journal_paper
- **Theme / reading status:** `GRN_structure_and_dynamics` / `bibliography_verified`
- **Source:** https://doi.org/10.1016/s0020-0190(00)00230-1
- **Actually inspected:** Not recorded beyond bibliography
- **Specific takeaway / limitation:** 仅核验作者、题名、年份及论文引用；未读原文摘要或正文，未从题名推断结论。

### BIO045 · 2022 — Attractor detection and enumeration algorithms for Boolean networks

- **Author / form:** Mori T; Akutsu T · journal_paper
- **Theme / reading status:** `GRN_structure_and_dynamics` / `abstract_read`
- **Source:** https://doi.org/10.1016/j.csbj.2022.05.027
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 综述有复杂度保证的同步吸引子检测算法及适用函数类，包括有界入度、AND/OR、nested canalizing。一般问题的复杂性与限制类的加速必须区分，不能对任意图承诺精确可扩展枚举。

### BIO046 · 2009 — Detecting a Singleton Attractor in a Boolean Network Utilizing SAT Algorithms

- **Author / form:** Takeyuki TAMURA; Tatsuya AKUTSU · journal_paper
- **Theme / reading status:** `GRN_structure_and_dynamics` / `bibliography_verified`
- **Source:** https://doi.org/10.1587/transfun.e92.a.493
- **Actually inspected:** Not recorded beyond bibliography
- **Specific takeaway / limitation:** 仅核验作者、题名、年份及论文引用；未读原文摘要或正文，未从题名推断结论。

### BIO047 · 2010 — Finding Attractors in Synchronous Multiple-Valued Networks Using SAT-Based Bounded Model Checking

- **Author / form:** Elena Dubrova; Maxim Teslenko; Liu Ming · conference_paper
- **Theme / reading status:** `GRN_structure_and_dynamics` / `bibliography_verified`
- **Source:** https://doi.org/10.1109/ISMVL.2010.35
- **Actually inspected:** Not recorded beyond bibliography
- **Specific takeaway / limitation:** 仅核验作者、题名、年份及论文引用；未读原文摘要或正文，未从题名推断结论。

### BIO048 · 1978 — Consistency in marked digraphs

- **Author / form:** Lowell W Beineke; Frank Harary · journal_paper
- **Theme / reading status:** `GRN_structure_and_dynamics` / `bibliography_verified`
- **Source:** https://doi.org/10.1016/0022-2496(78)90054-8
- **Actually inspected:** Not recorded beyond bibliography
- **Specific takeaway / limitation:** 仅核验作者、题名、年份及论文引用；未读原文摘要或正文，未从题名推断结论。

### BIO049 · 1953 — On the notion of balance of a signed graph

- **Author / form:** Frank Harary · journal_paper
- **Theme / reading status:** `GRN_structure_and_dynamics` / `bibliography_verified`
- **Source:** https://doi.org/10.1307/mmj/1028989917
- **Actually inspected:** Not recorded beyond bibliography
- **Specific takeaway / limitation:** 仅核验作者、题名、年份及论文引用；未读原文摘要或正文，未从题名推断结论。

### BIO050 · 2019 — Dynamics over Signed Networks

- **Author / form:** Guodong Shi; Claudio Altafini; John S. Baras · journal_paper
- **Theme / reading status:** `GRN_structure_and_dynamics` / `abstract_read`
- **Source:** https://doi.org/10.1137/17m1134172
- **Actually inspected:** Abstract (complete, indexed metadata)
- **Specific takeaway / limitation:** 比较 signed network 中 opposing 与 repelling 两类负边动力学，并用代数图论研究收敛。负边含义随模型改变；这里只把平衡性与符号变换作为相邻理论背景，不直接套用连续共识系统结论。

### BIO051 · 2025 — Signed Networks: theory, methods, and applications

- **Author / form:** Diaz-Diaz, Fernando; Candellone, Elena; Gonzalez-Casado, Miguel A.; Fraxanet, Emma; Vendeville, Antoine; Ferri, Irene; Teixeira, Andreia Sofia · preprint
- **Theme / reading status:** `GRN_structure_and_dynamics` / `abstract_read`
- **Source:** https://arxiv.org/abs/2511.17247
- **Actually inspected:** Abstract (complete, arXiv)
- **Specific takeaway / limitation:** 系统评述 signed graph 的平衡、frustration、模体、随机基准和动态过程。明确正负边承载不同作用而非简单有无关系。用于检查符号图术语；综述跨度大，不作为本仓库分类猜想的证明。

### BIO052 · 2025 — Low dimensionality of phenotypic space as an emergent property of coordinated teams in biological regulatory networks

- **Author / form:** Hari K; Harlapur P; Saxena A; Haldar K; Girish A; Malpani T; Levine H; Jolly MK · journal_paper
- **Theme / reading status:** `GRN_structure_and_dynamics` / `abstract_read`
- **Source:** https://doi.org/10.1016/j.isci.2024.111730
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 研究多个细胞命运网络及数据中的低维表型空间，并将 PC1 方差与互相抑制的节点团队强度联系。它提出的是具体结构统计关系，当前入度乘积目标无法识别这种团队结构。

### BIO053 · 2022 — Landscape of epithelial-mesenchymal plasticity as an emergent property of coordinated teams in regulatory networks

- **Author / form:** Hari K; Ullanat V; Balasubramanian A; Gopalan A; Jolly MK · journal_paper
- **Theme / reading status:** `GRN_structure_and_dynamics` / `abstract_read`
- **Source:** https://doi.org/10.7554/elife.76535
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 五种 EMT 网络中出现互相抑制的两组节点，且与终末表型的频率和鲁棒性相关。需要区分经验结构规律与对全部 signed graph 的定理；本次只读完整摘要。

### BIO054 · 2018 — Identification of the tumour transition states occurring during EMT

- **Author / form:** Pastushenko I; Brisebarre A; Sifrim A; Fioramonti M; Revenco T; Boumahdi S; Van Keymeulen A; Brown D; Moers V; Lemaire S; De Clercq S; Minguijón E; Balsat C; Sokolow Y; Dubois C; De Cock F; Scozzaro S; Sopena F; Lanas A; D&#x27;Haene N; Salmon I; Marine JC; Voet T; Sotiropoulou PA; Blanpain C · journal_paper
- **Theme / reading status:** `GRN_structure_and_dynamics` / `abstract_read`
- **Source:** https://doi.org/10.1038/s41586-018-0040-3
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 实验识别 EMT 的多个中间亚群及不同可塑性、侵袭性，表明二元终态编码可能丢失重要状态。此文提供生物边界条件，本次不对患者个体给出医学解释。

### BIO055 · 2022 — Robustness in phenotypic plasticity and heterogeneity patterns enabled by EMT networks

- **Author / form:** Hebbar A; Moger A; Hari K; Jolly MK · journal_paper
- **Theme / reading status:** `GRN_structure_and_dynamics` / `abstract_read`
- **Source:** https://doi.org/10.1016/j.bpj.2022.07.017
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 通过连续 Boolean 与参数随机化 ODE 两类方法研究 EMT 网络对拓扑、参数扰动的鲁棒性，并提出加权反馈指标。跨模型相似表现是经验支撑，仍需特定定义下的结构定理。

### BIO056 · 2020 — Multistability in the epithelial-mesenchymal transition network

- **Author / form:** Xin Y; Cummins B; Gedeon T · journal_paper
- **Theme / reading status:** `GRN_structure_and_dynamics` / `abstract_read`
- **Source:** https://doi.org/10.1186/s12859-020-3413-1
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 用 DSGRN 跨整个组合参数空间检查 EMT 中间稳态与多稳态，避免只改变少数参数的分岔扫描。适用结论针对给定网络及建模类别；参数块计数不能无条件解释为生物样本频率。

### BIO057 · 2017 — Number of Fixed Points and Disjoint Cycles in Monotone Boolean Networks

- **Author / form:** Aracena, Julio; Richard, Adrien; Salinas, Lilian · journal_paper
- **Theme / reading status:** `GRN_structure_and_dynamics` / `fulltext_sections_read`
- **Source:** https://doi.org/10.1137/16M1060868
- **Actually inspected:** Abstract；Introduction, principal bounds and exact/subgraph distinction；Cycle parameter definitions
- **Specific takeaway / limitation:** 已读摘要、引言主要结果与参数定义。以反馈顶点集 τ、互不相交环 ν 及带额外条件的 ν* 约束单调网络最多能有多少固定点。精确影响图要求下，达到 2^τ 当且仅当 ν*=τ；若允许忽略给定图的边，相应条件变成 ν=τ。由此可见‘精确图’与‘兼容图’会改变结构分类。本文优化单个网络的固定点数，仓库优化实现指定固定点集合的网络规则数，两者量词不同。

### BIO058 · 1933 — On the combination of subalgebras

- **Author / form:** Garrett Birkhoff · journal_paper
- **Theme / reading status:** `GRN_structure_and_dynamics` / `abstract_read`
- **Source:** https://doi.org/10.1017/s0305004100011464
- **Actually inspected:** Abstract (complete, indexed metadata)
- **Specific takeaway / limitation:** Birkhoff 的格论基础文献，从代数结构的公理研究组合问题。已读索引摘要，当前只作为单调函数格与理想表示的基础引用，没有从中提取新的 GRN 命题。

### BIO059 · 1998 — Necessary Conditions for Multistationarity and Stable Periodicity

- **Author / form:** El Houssine Snoussi · journal_paper
- **Theme / reading status:** `GRN_structure_and_dynamics` / `abstract_read`
- **Source:** https://doi.org/10.1142/s0218339098000042
- **Actually inspected:** Abstract (complete, indexed metadata)
- **Specific takeaway / limitation:** 对偏导符号固定的准单调微分系统证明正环是多稳态必要条件、含至少两个节点的负环是稳定周期必要条件。必要性不能倒置为充分性，且连续系统假设需与 Boolean 更新语义区分。

### BIO060 · 2020 — Multi-stability in cellular differentiation enabled by a network of three mutually repressing master regulators

- **Author / form:** Duddu AS; Sahoo S; Hati S; Jhunjhunwala S; Jolly MK · journal_paper
- **Theme / reading status:** `GRN_structure_and_dynamics` / `abstract_read`
- **Source:** https://doi.org/10.1098/rsif.2020.0631
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** toggle triad 可同时支持单阳性和双阳性表型；自激活可提高双阳性出现频率。说明‘多稳态数最大’与‘特定 single-high 集合出现概率最大’是不同优化目标。

### BIO061 · 2021 — Identification, visualization, statistical analysis and mathematical modeling of high-feedback loops in gene regulatory networks

- **Author / form:** Nordick B; Hong T · journal_paper
- **Theme / reading status:** `GRN_structure_and_dynamics` / `abstract_read`
- **Source:** https://doi.org/10.1186/s12859-021-04405-z
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** HiLoop 提取、可视化和统计高反馈子结构，并通过随机参数化探索多稳态与振荡。它可以为结构假设筛选案例，但该计算框架不提供任意规模的极值分类。

### BIO062 · 2022 — Network topology metrics explaining enrichment of hybrid epithelial/mesenchymal phenotypes in metastasis

- **Author / form:** Rashid M; Hari K; Thampi J; Santhosh NK; Jolly MK · journal_paper
- **Theme / reading status:** `GRN_structure_and_dynamics` / `abstract_read`
- **Source:** https://doi.org/10.1371/journal.pcbi.1010687
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 在 13 个 EMT 网络中比较混合表型、正负环和 frustration，发现相关性。可作为未来保留环结构目标的动机；本次不将相关性宣称为普遍因果定理。

### BIO063 · 2015 — A self-enforcing CD44s/ZEB1 feedback loop maintains EMT and stemness properties in cancer cells

- **Author / form:** Preca BT; Bajdak K; Mock K; Sundararajan V; Pfannstiel J; Maurer J; Wellner U; Hopt UT; Brummer T; Brabletz S; Brabletz T; Stemmler MP · journal_paper
- **Theme / reading status:** `GRN_structure_and_dynamics` / `abstract_read`
- **Source:** https://doi.org/10.1002/ijc.29642
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 实验研究 CD44s–ZEB1 自维持反馈及其与 EMT/干细胞样性质的关系。它给出具体正反馈机制作为生物背景；与全符号图规则数极值的直接数学联系尚未建立。

### BIO064 · 2013 — MicroRNA-based regulation of epithelial-hybrid-mesenchymal fate determination

- **Author / form:** Lu M; Jolly MK; Levine H; Onuchic JN; Ben-Jacob E · journal_paper
- **Theme / reading status:** `GRN_structure_and_dynamics` / `abstract_read`
- **Source:** https://doi.org/10.1073/pnas.1318192110
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 以 microRNA 特定调控机制建模，组合模块具有单稳态缓冲和三稳态开关等不同功能。主张根据机制选择函数类，避免把所有单调 Boolean 规则视为同等可实现。

### BIO065 · 2019 — Multistationarity in Structured Reaction Networks

- **Author / form:** Dickenstein A; Millán MP; Shiu A; Tang X · journal_paper
- **Theme / reading status:** `GRN_structure_and_dynamics` / `abstract_read`
- **Source:** https://doi.org/10.1007/s11538-019-00572-6
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 对具有显式稳态参数化的结构反应网络，用临界函数符号、代数消元和度理论判断多稳态并找参数见证。适用结构条件明确，不能直接套用为任意 GRN 的全参数判定。

### BIO066 · 2022 — Polynomial superlevel set representation of the multistationarity region of chemical reaction networks

- **Author / form:** Sadeghimanesh A; England M · journal_paper
- **Theme / reading status:** `GRN_structure_and_dynamics` / `abstract_read`
- **Source:** https://doi.org/10.1186/s12859-022-04921-6
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 用多项式超水平集表示反应网络多稳态参数区域，并比较常见表示方法。它提供连续模型可证近似的方向，与离散规则枚举属于不同技术任务。

### BIO067 · 2017 — Identifying parameter regions for multistationarity

- **Author / form:** Conradi C; Feliu E; Mincheva M; Wiuf C · journal_paper
- **Theme / reading status:** `GRN_structure_and_dynamics` / `abstract_read`
- **Source:** https://doi.org/10.1371/journal.pcbi.1005751
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 以 Brouwer 度和参数多项式系数符号划分唯一/多重平衡区域，避免纯抽样；在若干调控例子得到完整划分。关键在可执行的参数化结构，非对所有生物网络的统一算法。

### BIO068 · 2021 — Independent sets in the middle two layers of Boolean lattice

- **Author / form:** Balogh, József; Garcia, Ramon I.; Li, Lina · journal_paper
- **Theme / reading status:** `antichain_extremal_tools` / `abstract_read`
- **Source:** https://doi.org/10.1016/j.jcta.2020.105341
- **Actually inspected:** Abstract (complete, arXiv)
- **Specific takeaway / limitation:** 对奇数维 Boolean 格的中间两层独立集给出精细数量与典型结构，结合 Sapozhenko containers 与 polymer expansion。它是奇数 n 双相分析的直接技术先例，但并未计入本仓库的局部真假钉扎条件。

### BIO069 · 2024 — A Sharp Threshold for a Random Version of Sperner&#x27;s Theorem

- **Author / form:** Balogh, József; Krueger, Robert A. · journal_paper
- **Theme / reading status:** `antichain_extremal_tools` / `abstract_read`
- **Source:** https://doi.org/10.1002/rsa.21259
- **Actually inspected:** Abstract (complete, arXiv)
- **Specific takeaway / limitation:** 随机保留 Boolean 格元素时，p>3/4 的最大反链以高概率恰为中层，该阈值最优；还刻画 p>1/2 的最大反链。随机删元素与均匀抽整个反链是不同概率模型。

### BIO070 · 2015 — Independent sets in hypergraphs

- **Author / form:** Balogh, József; Morris, Robert; Samotij, Wojciech · preprint
- **Theme / reading status:** `antichain_extremal_tools` / `abstract_read`
- **Source:** https://arxiv.org/abs/1204.6530
- **Actually inspected:** Abstract (complete, arXiv)
- **Specific takeaway / limitation:** 以少量稀疏容器覆盖超图独立集，从而统一许多稀疏随机极值问题。可用于全局异常集合控制；局部稀有条件的相对概率需要额外分析，不能由容器数量直接读出。

### BIO071 · 2014 — A random version of Sperner&#x27;s theorem

- **Author / form:** Balogh, József; Mycroft, Richard; Treglown, Andrew · journal_paper
- **Theme / reading status:** `antichain_extremal_tools` / `abstract_read`
- **Source:** https://doi.org/10.1016/j.jcta.2014.08.003
- **Actually inspected:** Abstract (complete, arXiv)
- **Specific takeaway / limitation:** 当 pn 趋于无穷时，随机 Boolean 子格的最大反链大小渐近为中层的期望大小，解决 Osthus 猜想。原始参考文献将题名写成 sparse version，已按作者与期刊更正为 random version，未重复计数。

### BIO072 · 2016 — Applications of graph containers in the boolean lattice

- **Author / form:** Balogh, Jozsef; Treglown, Andrew; Wagner, Adam Zsolt · preprint
- **Theme / reading status:** `antichain_extremal_tools` / `abstract_read`
- **Source:** https://arxiv.org/abs/1602.05870
- **Actually inspected:** Abstract (complete, arXiv)
- **Specific takeaway / limitation:** 应用图容器证明 Boolean 格中的计数、编码与随机相交族结果，并给出两个旧猜想的反例。对本项目的启示是先检查极值族稳定性，再进行计数；这些反例是作者成果。

### BIO073 · 1984 — A short course on cluster expansions

- **Author / form:** D. C. Brydges · lecture_course_chapter
- **Theme / reading status:** `antichain_extremal_tools` / `bibliography_verified`
- **Source:** https://arxiv.org/html/2411.03400v2#bib
- **Actually inspected:** Not recorded beyond bibliography
- **Specific takeaway / limitation:** 仅核验作者、题名、年份及论文引用；未读原文摘要或正文，未从题名推断结论。

### BIO074 · 2016 — Maximum-size antichains in random set-systems

- **Author / form:** Neto, Maurício Collares; Morris, Robert · journal_paper
- **Theme / reading status:** `antichain_extremal_tools` / `abstract_read`
- **Source:** https://doi.org/10.1002/rsa.20647
- **Actually inspected:** Abstract (complete, arXiv)
- **Specific takeaway / limitation:** 随机集合族中不存在 k-chain 的最大子族在 pn→∞ 时具有 (k−1) 倍中层大小的渐近式。它研究最大基数而非满足指定局部约束的族总数，提供的是技术参照。

### BIO075 · 2026 — Dedekind&#x27;s problem in the hypergrid

- **Author / form:** Falgas-Ravry, Victor; Räty, Eero; Tomon, István · journal_paper
- **Theme / reading status:** `antichain_extremal_tools` / `abstract_read`
- **Source:** https://doi.org/10.1016/j.aim.2026.110796
- **Actually inspected:** Abstract (complete, arXiv)
- **Specific takeaway / limitation:** 对多值格 [t]^n 的反链数，给出对任意 t 相对 n 都适用的接近宽度上界，误差 O(log³n/n)。这可支持多值扩展的首阶熵，但不足以分辨相邻 GRN 极值候选。

### BIO076 · 2010 — A Threshold Phenomenon for Random Independent Sets in the Discrete Hypercube

- **Author / form:** DAVID GALVIN · journal_paper
- **Theme / reading status:** `antichain_extremal_tools` / `abstract_read`
- **Source:** https://doi.org/10.1017/s0963548310000155
- **Actually inspected:** Abstract (complete, indexed metadata)
- **Specific takeaway / limitation:** 超立方体 hard-core 模型在 fugacity 约为 1 时，小侧缺陷出现发生锐变；还给出条件于某顶点被占据的远程影响。相关性问题与当前局部条件计数接近，但图与测度需重新对应。

### BIO077 · 2019 — Independent sets in the discrete hypercube

- **Author / form:** Galvin, David · preprint
- **Theme / reading status:** `antichain_extremal_tools` / `abstract_read`
- **Source:** https://arxiv.org/abs/1901.01991
- **Actually inspected:** Abstract (complete, arXiv)
- **Specific takeaway / limitation:** 整理 Sapozhenko 对超立方体独立集数渐近式的证明。它是自学精细计数工具的简明入口；该独立集图不等同于完整 Boolean 格的可比图。

### BIO078 · 1954 — Lattice Theoretic Properties of Frontal Switching Functions

- **Author / form:** E. N. Gilbert · journal_paper
- **Theme / reading status:** `antichain_extremal_tools` / `bibliography_verified`
- **Source:** https://doi.org/10.1002/sapm195433157
- **Actually inspected:** Not recorded beyond bibliography
- **Specific takeaway / limitation:** 仅核验作者、题名、年份及论文引用；未读原文摘要或正文，未从题名推断结论。

### BIO079 · 1966 — Sur le nombre des fonctions booléennes monotones de n variables

- **Author / form:** G. Hansel · journal_paper
- **Theme / reading status:** `antichain_extremal_tools` / `bibliography_verified`
- **Source:** https://arxiv.org/html/2411.03400v2#bib
- **Actually inspected:** Not recorded beyond bibliography
- **Specific takeaway / limitation:** 仅核验作者、题名、年份及论文引用；未读原文摘要或正文，未从题名推断结论。

### BIO080 · 2019 — Algorithmic Pirogov–Sinai theory

- **Author / form:** Helmuth, Tyler; Perkins, Will; Regts, Guus · journal_paper
- **Theme / reading status:** `antichain_extremal_tools` / `abstract_read`
- **Source:** https://doi.org/10.1007/s00440-019-00928-y
- **Actually inspected:** Abstract (complete, arXiv)
- **Specific takeaway / limitation:** 将 Pirogov–Sinai 轮廓与截断 Taylor 展开结合，在若干低温模型上构造近似计数和采样算法。提供控制相内缺陷的思路；其低温与边界条件应逐一检查。

### BIO081 · 2020 — Algorithms for #BIS-Hard Problems on Expander Graphs

- **Author / form:** Matthew Jenssen; Peter Keevash; Will Perkins · journal_paper
- **Theme / reading status:** `antichain_extremal_tools` / `abstract_read`
- **Source:** https://doi.org/10.1137/19m1286669
- **Actually inspected:** Abstract (complete, indexed metadata)
- **Specific takeaway / limitation:** 在有界度二分扩展图的高 fugacity hard-core 模型等条件下构造 FPTAS 和采样。可作为验证条件分区函数的算法参照；不能略去扩展性或活动参数阈值。

### BIO082 · 2026 — A Refined Graph Container Lemma and Applications to the Hard‐Core Model on Bipartite Expanders

- **Author / form:** Jenssen, Matthew; Malekshahian, Alexandru; Park, Jinyoung · journal_paper
- **Theme / reading status:** `antichain_extremal_tools` / `abstract_read`
- **Source:** https://doi.org/10.1002/rsa.70041
- **Actually inspected:** Abstract (complete, arXiv)
- **Specific takeaway / limitation:** 改进图容器引理，将高维超立方体 structured phase 与算法适用活动参数范围推进到 log²d/√d 量级。它支撑 JMP 的精细分析，不直接给出本仓库局部条件概率的比例公式。

### BIO083 · 2020 — Independent sets in the hypercube revisited

- **Author / form:** Jenssen, Matthew; Perkins, Will · journal_paper
- **Theme / reading status:** `antichain_extremal_tools` / `abstract_read`
- **Source:** https://doi.org/10.1112/jlms.12331
- **Actually inspected:** Abstract (complete, arXiv)
- **Specific takeaway / limitation:** 将容器方法与 polymer cluster expansion 结合，得到独立集的更精确渐近及典型缺陷统计。这是‘首阶中层数打平后比较小缺陷’的直接方法论来源。

### BIO084 · 2022 — Independent sets of a given size and structure in the hypercube

- **Author / form:** Matthew Jenssen; Will Perkins; Aditya Potukuchi · journal_paper
- **Theme / reading status:** `antichain_extremal_tools` / `abstract_read`
- **Source:** https://doi.org/10.1017/s0963548321000559
- **Actually inspected:** Abstract (complete, indexed metadata)
- **Specific takeaway / limitation:** 对固定密度的超立方体独立集计数给出渐近，并建立结构量的多元局部中心极限定理。提示可在固定大小/加权测度下研究 GRN 规则；当前均匀单调函数版本尚未推广到此条件。

### BIO085 · 2002 — Entropy, independent sets and antichains: A new approach to Dedekind’s problem

- **Author / form:** Jeff Kahn · journal_paper
- **Theme / reading status:** `antichain_extremal_tools` / `abstract_read`
- **Source:** https://doi.org/10.1090/s0002-9939-01-06058-0
- **Actually inspected:** Complete abstract in author institution repository
- **Specific takeaway / limitation:** 熵方法给出正则二分图带两侧权重的独立集分区函数界，并推广到分层偏序，简化 Kleitman–Markowsky 估计。其首阶/熵界解释了仓库边界排除，但不提供相邻中心候选的微小比值。

### BIO086 · 1966 — A Theorem of Finite Sets

- **Author / form:** G. Katona · research_chapter_original_1966_reprint_2009
- **Theme / reading status:** `antichain_extremal_tools` / `bibliography_verified`
- **Source:** https://doi.org/10.1007/978-0-8176-4842-8_27
- **Actually inspected:** Not recorded beyond bibliography
- **Specific takeaway / limitation:** 仅核验作者、题名、年份及论文引用；未读原文摘要或正文，未从题名推断结论。

### BIO087 · 1969 — On Dedekind&#x27;s Problem: The Number of Monotone Boolean Functions

- **Author / form:** Daniel Kleitman · journal_paper
- **Theme / reading status:** `antichain_extremal_tools` / `bibliography_verified`
- **Source:** https://doi.org/10.2307/2036446
- **Actually inspected:** Not recorded beyond bibliography
- **Specific takeaway / limitation:** 仅核验作者、题名、年份及论文引用；未读原文摘要或正文，未从题名推断结论。

### BIO088 · 1975 — On Dedekind&#x27;s Problem: The Number of Isotone Boolean Functions. II

- **Author / form:** D. Kleitman; G. Markowsky · journal_paper
- **Theme / reading status:** `antichain_extremal_tools` / `bibliography_verified`
- **Source:** https://doi.org/10.2307/1998052
- **Actually inspected:** Not recorded beyond bibliography
- **Specific takeaway / limitation:** 仅核验作者、题名、年份及论文引用；未读原文摘要或正文，未从题名推断结论。

### BIO089 · 2002 — The Width of Random Subsets of Boolean Lattices

- **Author / form:** Y. Kohayakawa; B. Kreuter · journal_paper
- **Theme / reading status:** `antichain_extremal_tools` / `bibliography_verified`
- **Source:** https://doi.org/10.1006/jcta.2002.3293
- **Actually inspected:** Not recorded beyond bibliography
- **Specific takeaway / limitation:** 仅核验作者、题名、年份及论文引用；未读原文摘要或正文，未从题名推断结论。

### BIO090 · 1965 — On monotone functions of the algebra of logic

- **Author / form:** V. K. Korobkov · journal_paper
- **Theme / reading status:** `antichain_extremal_tools` / `bibliography_verified`
- **Source:** https://arxiv.org/html/2411.03400v2#bib
- **Actually inspected:** Not recorded beyond bibliography
- **Specific takeaway / limitation:** 仅核验作者、题名、年份及论文引用；未读原文摘要或正文，未从题名推断结论。

### BIO091 · 1981 — The number of monotone Boolean functions

- **Author / form:** A. D. Korshunov · journal_paper
- **Theme / reading status:** `antichain_extremal_tools` / `bibliography_verified`
- **Source:** https://www.mathnet.ru/eng/person13594
- **Actually inspected:** Not recorded beyond bibliography
- **Specific takeaway / limitation:** 仅核验作者、题名、年份及论文引用；未读原文摘要或正文，未从题名推断结论。

### BIO092 · 2002 — On the distribution of the number of monotone Boolean functions relative to the number of lower units

- **Author / form:** A.D. Korshunov; I. Shmulevich · journal_paper
- **Theme / reading status:** `antichain_extremal_tools` / `bibliography_verified`
- **Source:** https://doi.org/10.1016/s0012-365x(02)00507-1
- **Actually inspected:** Not recorded beyond bibliography
- **Specific takeaway / limitation:** 仅核验作者、题名、年份及论文引用；未读原文摘要或正文，未从题名推断结论。

### BIO093 · 1986 — Cluster expansion for abstract polymer models

- **Author / form:** Roman Kotecký; David Preiss · journal_paper
- **Theme / reading status:** `antichain_extremal_tools` / `abstract_read`
- **Source:** https://doi.org/10.1007/BF01211762
- **Actually inspected:** Abstract (publisher, complete)
- **Specific takeaway / limitation:** 在抽象 polymer 系统中给出簇展开收敛的直接证明。它为局部钉扎后的级数与余项估计提供工具；需要核对不相容关系、正权重及收敛控制，原文没有直接比较 GRN 候选计数。已读出版社完整摘要。

### BIO094 · 2022 — Independent sets in random subgraphs of the hypercube

- **Author / form:** Kronenberg, Gal; Spinka, Yinon · preprint
- **Theme / reading status:** `antichain_extremal_tools` / `abstract_read`
- **Source:** https://arxiv.org/abs/2201.06127
- **Actually inspected:** Abstract (complete, arXiv)
- **Specific takeaway / limitation:** 研究随机删边的超立方体独立集数，并扩展到 hard-core 模型；通过相关反铁磁 Ising 表达控制随机结构。用于未来拓扑不确定性的技术背景，本次仅读摘要。

### BIO095 · 1963 — The number of simplices in a complex

- **Author / form:** J. B. Kruskal · research_chapter
- **Theme / reading status:** `antichain_extremal_tools` / `bibliography_verified`
- **Source:** https://arxiv.org/html/2411.03400v2#bib
- **Actually inspected:** Not recorded beyond bibliography
- **Specific takeaway / limitation:** 仅核验作者、题名、年份及论文引用；未读原文摘要或正文，未从题名推断结论。

### BIO096 · 2025 — The Number of Colorings of the Middle Layers of the Hamming Cube

- **Author / form:** Li, Lina; McKinley, Gweneth; Park, Jinyoung · journal_paper
- **Theme / reading status:** `antichain_extremal_tools` / `abstract_read`
- **Source:** https://doi.org/10.1007/s00493-024-00128-w
- **Actually inspected:** Abstract (complete, arXiv)
- **Specific takeaway / limitation:** 对 Boolean 格中间两层的 q-着色给出数量和典型结构，联合熵、容器和 polymer 展开。多相竞争的工具可能适用于多表型编码，但不能直接解释当前二值局部约束。

### BIO097 · 2000 — Maximum antichains in random subsets of a finite set

- **Author / form:** D. Osthus · journal_paper
- **Theme / reading status:** `antichain_extremal_tools` / `bibliography_verified`
- **Source:** https://arxiv.org/html/2411.03400v2#bib
- **Actually inspected:** Not recorded beyond bibliography
- **Specific takeaway / limitation:** 仅核验作者、题名、年份及论文引用；未读原文摘要或正文，未从题名推断结论。

### BIO098 · 2025 — Note on the number of antichains in generalizations of the boolean lattice

- **Author / form:** Jinyoung Park; Michail Sarantis; Prasad Tetali · journal_paper
- **Theme / reading status:** `antichain_extremal_tools` / `bibliography_verified`
- **Source:** https://doi.org/10.5070/c65165018
- **Actually inspected:** Not recorded beyond bibliography
- **Specific takeaway / limitation:** 仅核验作者、题名、年份及论文引用；未读原文摘要或正文，未从题名推断结论。

### BIO099 · 2017 — Deterministic Polynomial-Time Approximation Algorithms for Partition Functions and Graph Polynomials

- **Author / form:** Viresh Patel; Guus Regts · journal_paper
- **Theme / reading status:** `antichain_extremal_tools` / `abstract_read`
- **Source:** https://doi.org/10.1137/16m1101003
- **Actually inspected:** Abstract (complete, indexed metadata)
- **Specific takeaway / limitation:** 在有界度图和图多项式无零圆盘条件下，用截断展开建立确定性近似算法。这里‘无零’是核心假设；未经验证不应称作一般条件计数算法。

### BIO100 · 1999 — Entropy and enumeration of Boolean functions

- **Author / form:** H. Pippenger · journal_paper
- **Theme / reading status:** `antichain_extremal_tools` / `bibliography_verified`
- **Source:** https://doi.org/10.1109/18.782146
- **Actually inspected:** Not recorded beyond bibliography
- **Specific takeaway / limitation:** 仅核验作者、题名、年份及论文引用；未读原文摘要或正文，未从题名推断结论。

### BIO101 · 1987 — On the number of connected subsets with given cardinality of the boundary in bipartite graphs

- **Author / form:** A. A. Sapozhenko · journal_paper
- **Theme / reading status:** `antichain_extremal_tools` / `bibliography_verified`
- **Source:** https://arxiv.org/html/2411.03400v2#bib
- **Actually inspected:** Not recorded beyond bibliography
- **Specific takeaway / limitation:** 仅核验作者、题名、年份及论文引用；未读原文摘要或正文，未从题名推断结论。

### BIO102 · 1991 — On the number of antichains in multilevelled ranked posets

- **Author / form:** A. A. SAPOZHENKO · journal_paper
- **Theme / reading status:** `antichain_extremal_tools` / `bibliography_verified`
- **Source:** https://doi.org/10.1515/dma.1991.1.2.149
- **Actually inspected:** Not recorded beyond bibliography
- **Specific takeaway / limitation:** 仅核验作者、题名、年份及论文引用；未读原文摘要或正文，未从题名推断结论。

### BIO103 · 2015 — Hypergraph containers

- **Author / form:** Saxton, David; Thomason, Andrew · journal_paper
- **Theme / reading status:** `antichain_extremal_tools` / `abstract_read`
- **Source:** https://doi.org/10.1007/s00222-014-0562-8
- **Actually inspected:** Abstract (complete, arXiv)
- **Specific takeaway / limitation:** 以少量受控集合覆盖超图的全部独立集，建立可用于计数、着色和稀疏随机极值的容器理论。对本仓库提供全局异常集合上界，但极稀有局部条件的相对误差仍需单独分析。期刊原文与 arXiv 仅计一个研究工作。

### BIO104 · 2005 — The repulsive lattice gas, the independent-set polynomial, and the Lovász local lemma

- **Author / form:** Alexander D. Scott; Alan D. Sokal · journal_paper
- **Theme / reading status:** `antichain_extremal_tools` / `bibliography_verified`
- **Source:** https://doi.org/10.1007/s10955-004-2055-4
- **Actually inspected:** Not recorded beyond bibliography
- **Specific takeaway / limitation:** 仅核验作者、题名、年份及论文引用；未读原文摘要或正文，未从题名推断结论。

### BIO105 · 1928 — Ein Satz über Untermengen einer endlichen Menge

- **Author / form:** E. Sperner · journal_paper
- **Theme / reading status:** `antichain_extremal_tools` / `bibliography_verified`
- **Source:** https://arxiv.org/html/2411.03400v2#bib
- **Actually inspected:** Not recorded beyond bibliography
- **Specific takeaway / limitation:** 仅核验作者、题名、年份及论文引用；未读原文摘要或正文，未从题名推断结论。

### BIO106 · 2023 — A computation of D(9) using FPGA Supercomputing

- **Author / form:** Van Hirtum, Lennart; De Causmaecker, Patrick; Goemaere, Jens; Kenter, Tobias; Riebler, Heinrich; Lass, Michael; Plessl, Christian · preprint
- **Theme / reading status:** `antichain_extremal_tools` / `abstract_read`
- **Source:** https://arxiv.org/abs/2304.03039
- **Actually inspected:** Abstract (complete, arXiv)
- **Specific takeaway / limitation:** 通过 FPGA 与集群计算 D(9)，提供约 4.9 亿个可独立检查的分项和总和。此项记录用于计算可核验性背景，与 Jäkel 的独立方法为两篇不同论文；没有把数据下载当作论文阅读。

### BIO107 · 1991 — A computation of the eighth Dedekind number

- **Author / form:** Doug Wiedemann · journal_paper
- **Theme / reading status:** `antichain_extremal_tools` / `bibliography_verified`
- **Source:** https://doi.org/10.1007/bf00385808
- **Actually inspected:** Not recorded beyond bibliography
- **Specific takeaway / limitation:** 仅核验作者、题名、年份及论文引用；未读原文摘要或正文，未从题名推断结论。

### BIO108 · 2026 — Gene Regulatory Networks that Support Multi-fate Cellular Decisions

- **Author / form:** Harshavardhan BV; Adigwe S; Jolly MK; Gedeon T · journal_paper
- **Theme / reading status:** `Boolean_network_theory` / `fulltext_sections_read`
- **Source:** https://doi.org/10.1007/s11538-026-01791-4
- **Actually inspected:** Abstract；Model definitions；Section 6, particularly 6.3；Discussion
- **Specific takeaway / limitation:** 已读摘要、模型定义、同时多稳态问题所在 §6、特别是 §6.3，以及讨论与参考文献。论文区分单个 single-high 状态的流行度、equipotency 与同时保持全部 single-high 状态。仓库对应第三者在完整符号图、正自环和允许冗余输入时的局部计数问题。固定图的计数等于每节点计数乘积，因此仅依赖抑制入度序列；同入度的环、模块和互反结构在此观测量下严格不可区分。§6.3 留下 n>5 最优抑制输入数的一般问题。这个具体问题于 2026 年提出，不能称为已经困扰生物学界几十年的同一命题。我们的中央窗口推论处理其渐近定位，仍未完成有限 n 分类。

### BIO109 · 2026 — On Dedekind&#x27;s problem, a sparse version of Sperner&#x27;s theorem, and antichains of a given size in the Boolean lattice

- **Author / form:** Jenssen, Matthew; Malekshahian, Alexandru; Park, Jinyoung · journal_paper
- **Theme / reading status:** `Boolean_network_theory` / `proof_audited`
- **Source:** https://doi.org/10.1112/jlms.70624
- **Actually inspected:** Theorem 1.7；Equations (3.6), (4.4)；Section 5 sampling；Lemma 6.1；Corollary 7.10；Relevant proof dependencies for the central-window corollary
- **Specific takeaway / limitation:** 已核查 Theorem 1.7、式 (3.6)/(4.4)、§5 采样、Lemma 6.1、Corollary 7.10 及其用于本推论的假设。全体反链有 exp(−Ω(n²)) 的中层外质量；偶数为一个三层相，奇数由两个三层相混合。正权 polymer 模型中 P(γ 被占据)≤wγ，结合局部总权控制，可使 O(n) 个指定中层比特以至少 2^(−O(n)) 的概率同时满足 GRN 条件。这一步弥补了仅比较 2^中层自由数 与 D(n) 时无法控制稀有条件的缺口。完整推论在 central_window_proof.md。全文其他部分如固定大小反链的所有局部极限定理没有逐一审计，不标为整篇证明已核验。结尾 Conjecture 9.1/9.2 涉及更稀疏密度下的层数结构，是作者原有问题。

### BIO110 · 2024 — A meta-analysis of Boolean network models reveals design principles of gene regulatory networks

- **Author / form:** Kadelka, Claus; Butrie, Taras-Michael; Hilton, Evan; Kinseth, Jack; Schmidt, Addison; Serdarevic, Haris · journal_paper
- **Theme / reading status:** `Boolean_network_theory` / `fulltext_sections_read`
- **Source:** https://doi.org/10.1126/sciadv.adj0822
- **Actually inspected:** Abstract；Conclusion；Limitations paragraphs
- **Specific takeaway / limitation:** 已读摘要和结论/限制部分。策展 Boolean 模型集合显示 canalization、功能冗余及稳定性等设计特征；作者明确讨论二元表达限制、数据库完整性无法保证、物种/过程选择偏差和建模者偏差，且动物模型占多数。因此不能据这类数据断言所有 GRN 均服从均匀单调函数测度。后续最有用的检验是比较明确先验和动态指标，而非把‘更普遍的规则数’直接解释为进化选择。

### BIO111 · 2023 — Theoretical and computational tools to model multistable gene regulatory networks

- **Author / form:** Bocci, Federico; Jia, Dongya; Nie, Qing; Jolly, Mohit Kumar; Onuchic, Jose · journal_paper
- **Theme / reading status:** `Boolean_network_theory` / `fulltext_sections_read`
- **Source:** https://doi.org/10.1088/1361-6633/acec88
- **Actually inspected:** Abstract；Introduction；Selected modeling background；Section 4 concluding challenges
- **Specific takeaway / limitation:** 已读摘要、引言、部分方法背景及结论 §4。文章比较随机化学反应、连续动力学、参数随机化和 Boolean 模型，并强调问题不同应选不同描述。讨论特别指出转录后过程、单细胞数据中的网络推断、力学与化学反馈等未充分整合问题。这些是生物建模挑战，不是可直接宣称由当前计数定理解决的难题。

### BIO112 · 2026 — K-Independent Boolean Networks

- **Author / form:** Aracena, Julio; Astete-Elguin, Raúl · journal_paper
- **Theme / reading status:** `Boolean_network_theory` / `fulltext_sections_read`
- **Source:** https://doi.org/10.1137/24M1700600
- **Actually inspected:** ArXiv abstract and introduction；Section 2.1, Theorem 2.5, Corollaries and Remark 2.8；Section 3, Steiner construction and proof；Section 4 questions
- **Specific takeaway / limitation:** 已读 arXiv 版本的引言、§2.1 定理及反例说明、§3 的 Steiner 系统构造及证明、§4 问题。k-independence 要求固定点集合对任意 k 个坐标的投影满射，是覆盖数组条件，比单高集合不同。无自环条件下，k-independence 强迫入度与函数 implicant 复杂度至少 k，AND/OR 类因而受限；文中明确讨论加自环可破坏这些结论。单调完整影响图的构造用组合设计实现。不能把摘要中 unate 的 n/2 上限移植到本仓库的全正自环、允许冗余输入版本。对最终期刊版只核验书目，未把预印本的所有开放问题当作 2026 已确认未解。

### BIO113 · 2018 — Fixed points and connections between positive and negative cycles in Boolean networks

- **Author / form:** Richard, Adrien · preprint
- **Theme / reading status:** `Boolean_network_theory` / `fulltext_sections_read`
- **Source:** https://arxiv.org/abs/1509.07702
- **Actually inspected:** Introduction；Theorems 1–6；Structural assumptions and definitions
- **Specific takeaway / limitation:** 已读引言、Theorems 1–6 和其结构条件。论文改进正负环存在性条件：若每个正环有一条边，使删边后的某个非平凡初始强连通分量包含终点且只有负环，则固定点至多一个；负环有对偶存在性结论。其他结果加入入度和 canalization 条件。它显示环间连接可决定固定点存在/唯一性。我们的局部函数计数乘积没有表达这些连接，不能从该计数直接生成一般拓扑分类。此处没有把作者证明后的结果列为未解问题。

### BIO114 · 2015 — Fixed point theorems for Boolean networks expressed in terms of forbidden subnetworks

- **Author / form:** Richard, Adrien · journal_paper
- **Theme / reading status:** `Boolean_network_theory` / `fulltext_sections_read`
- **Source:** https://doi.org/10.1016/j.tcs.2015.03.038
- **Actually inspected:** Abstract；Introduction；Subnetwork and non-expansive definitions
- **Specific takeaway / limitation:** 已读摘要、完整引言和 subnetwork/non-expansive 定义。subnetwork 通过将部分变量钉为 0/1 获得；所有 subnetwork 均有唯一固定点可用禁止某类 even/odd self-dual 网络刻画。对非扩张类，禁止正/负环子网络分别给出至多/至少一个固定点的精确对应。定理量词覆盖所有钉扎，不只原网络自身。它提供未来研究固定输入或干预鲁棒性时的结构语言；本次没有重证全部分类证明。

### BIO115 · 2013 — From kernels in directed graphs to fixed points and negative cycles in Boolean networks

- **Author / form:** Adrien Richard; Paul Ruet · journal_paper
- **Theme / reading status:** `Boolean_network_theory` / `bibliography_verified`
- **Source:** https://doi.org/10.1016/j.dam.2012.10.022
- **Actually inspected:** Not recorded beyond bibliography
- **Specific takeaway / limitation:** 仅核验作者、题名、年份及论文引用；未读原文摘要或正文，未从题名推断结论。

### BIO116 · 2022 — Complexity of fixed point counting problems in Boolean networks

- **Author / form:** Bridoux, Florian; Durbec, Amélia; Perrot, Kévin; Richard, Adrien · journal_paper
- **Theme / reading status:** `Boolean_network_theory` / `fulltext_sections_read`
- **Source:** https://doi.org/10.1016/j.jcss.2022.01.004
- **Actually inspected:** Abstract；Sections 1.1–1.2；Exact signed interaction digraph definition；Section 7 conclusion and conjecture
- **Specific takeaway / limitation:** 已读摘要、§1.1–1.2、精确 SID 定义与 §7。对给定 signed interaction digraph，问是否存在兼容且有至少/至多 k 个固定点的函数，复杂性随 k 与入度约束从 P 到 NP、NP^NP、NP^#P、NEXPTIME。该图要求记录真正有效的依赖。§7 明确猜测全正 SID 的固定 k-MaxFPP 存在 P/NP 分界 k0，并提出允许忽略部分边可能改变复杂性。这里只记录 2022 原文猜测；本次尚未穷尽其后所有引文，不能宣布其截至今日仍无人解决。

### BIO117 · 2011 — Local negative circuits and fixed points in non-expansive Boolean networks

- **Author / form:** Richard, Adrien · journal_paper
- **Theme / reading status:** `Boolean_network_theory` / `fulltext_sections_read`
- **Source:** https://doi.org/10.1016/j.dam.2011.01.010
- **Actually inspected:** Abstract；Introduction；Theorems 1–4
- **Specific takeaway / limitation:** 已读摘要、引言和 Theorems 1–4。局部离散 Jacobian 无环时有唯一固定点；局部无正环给至多一个固定点。作者对局部无负环的存在性问题，在每点每顶点出度至多一、或所有正环共同经过某顶点等额外条件下证明部分结果。关键是局部影响图与全局并图的差别；不能把全局无负环的已知定理替换为无附加条件的局部陈述。旧文提出的问题不自动是 2026 新研究目标。

### BIO118 · 2010 — Topological fixed points in Boolean networks

- **Author / form:** Loïc Paulevé; Adrien Richard · journal_paper
- **Theme / reading status:** `Boolean_network_theory` / `abstract_read`
- **Source:** https://doi.org/10.1016/j.crma.2010.07.014
- **Actually inspected:** Abstract (complete, indexed metadata)
- **Specific takeaway / limitation:** 定义对所有同影响图 Boolean 规则均成立的拓扑固定点，并根据图结构分类。这是对所有规则的普遍量词，与本仓库‘满足目标的规则数最多’的量词不同。

### BIO119 · 2018 — On Fixable Families of Boolean Networks

- **Author / form:** Gadouleau, Maximilien; Richard, Adrien · conference_paper
- **Theme / reading status:** `Boolean_network_theory` / `fulltext_sections_read`
- **Source:** https://doi.org/10.1007/978-3-319-99813-8_36
- **Actually inspected:** Abstract；Introduction and notation；Section 3, Lemma 1 proof and Theorem 2
- **Specific takeaway / limitation:** 已读摘要、引言、定义、§3 Lemma 1 与 Theorem 2 附近证明。fixing word 是一个更新变量序列，能把所有初态送到固定点；对整个函数族，要求同一序列适用于每个成员。异步无环族的最短通用字长为 Θ(n2^n)，单调族已有 O(n³) 上界，某些树/对称合取图族可达线性或二次。它把‘存在固定点’推进到‘能否统一抵达’并显示代价差别；完全单调与节点各自可补成单调的 unate 类不能混淆。

### BIO120 · 2024 — Biologically meaningful regulatory logic enhances the convergence rate in Boolean networks and bushiness of their state transition graph

- **Author / form:** Sil P; Subbaroyan A; Kulkarni S; Martin OC; Samal A · journal_paper
- **Theme / reading status:** `Boolean_network_theory` / `abstract_read`
- **Source:** https://doi.org/10.1093/bib/bbae150
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 在网络结构与生物吸引子固定时改变 Boolean 函数类别，研究状态转移图的汇聚和收缩性质，并寻找局部灵敏度及瞬态长度的代理指标。生物规则可有相同固定点而不同动态，直接说明只计 fixed points 对动力学解释不充分。本次读完整摘要，未审计所有实验与代理指标。

### BIO121 · 2020 — Reconciling qualitative, abstract, and scalable modeling of biological networks

- **Author / form:** Chatain, Thomas; Haar, Stefan; Kol{č}ák, Juraj; Paulevé, Loïc · journal_paper
- **Theme / reading status:** `Boolean_network_theory` / `fulltext_sections_read`
- **Source:** https://doi.org/10.1038/s41467-020-18112-5
- **Actually inspected:** Journal abstract；Companion technical report refinement definitions；Theorem 3；Proposition 5 and proof；Theorem 4 and proof；Discussion
- **Specific takeaway / limitation:** 阅读期刊摘要及配套 arXiv:1808.10240 技术证明中的 refinement 定义、可达性 Theorem 3、最小 trap space 对应 Proposition 5、Theorem 4 与讨论。该语义以四种局部状态抽象多值细化，固定点保持不变，非固定点动态可增加。局部单调函数下可达性可在多项式时间处理，MP 吸引子对应最小 trap spaces；这些结论不意味着异步吸引子也总是一一对应。技术报告与期刊正文按同一研究工作合并计数。

### BIO122 · 2012 — Static Analysis of Boolean Networks Based on Interaction Graphs: A Survey

- **Author / form:** Loïc Paulevé; Adrien Richard · journal_paper
- **Theme / reading status:** `Boolean_network_theory` / `bibliography_verified`
- **Source:** https://doi.org/10.1016/j.entcs.2012.05.017
- **Actually inspected:** Not recorded beyond bibliography
- **Specific takeaway / limitation:** 仅核验作者、题名、年份及论文引用；未读原文摘要或正文，未从题名推断结论。

### BIO123 · 2019 — Positive and negative cycles in Boolean networks

- **Author / form:** Richard A · journal_paper
- **Theme / reading status:** `Boolean_network_theory` / `abstract_read`
- **Source:** https://doi.org/10.1016/j.jtbi.2018.11.028
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 综述正负反馈环在异步 Boolean 网络中的影响和 Thomas 规则。作为语义与必要条件的校准来源；本次只读完整摘要，未把综述中的所有定理标作已审计。

### BIO124 · 2008 — Maximum number of fixed points in regulatory Boolean networks

- **Author / form:** Aracena J · journal_paper
- **Theme / reading status:** `Boolean_network_theory` / `abstract_read`
- **Source:** https://doi.org/10.1007/s11538-008-9304-7
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 在 regulatory Boolean 网络中，以正反馈顶点集的最小大小给出固定点数上界。它研究单个函数可有多少固定点，与指定固定点集合能由多少函数实现不同。

### BIO125 · 2021 — Finding the fixed points of a Boolean network from a positive feedback vertex set

- **Author / form:** Aracena J; Cabrera-Crot L; Salinas L · journal_paper
- **Theme / reading status:** `Boolean_network_theory` / `abstract_read`
- **Source:** https://doi.org/10.1093/bioinformatics/btaa922
- **Actually inspected:** Abstract (complete, Europe PMC structured record)
- **Specific takeaway / limitation:** 给出基于正反馈顶点集 P 的固定点枚举算法，其代价含 2^{|P|} 及函数求值成本。其优势来自小正反馈顶点集；完全带正自环图中这一参数不小，不能期待自动避免指数代价。

### BIO126 · 2023 — Marker and source-marker reprogramming of Most Permissive Boolean networks and ensembles with BoNesis

- **Author / form:** Paulevé, Loïc · journal_paper
- **Theme / reading status:** `Boolean_network_theory` / `fulltext_sections_read`
- **Source:** https://doi.org/10.24072/pcjournal.255
- **Actually inspected:** Abstract；Four reprogramming problem definitions；Complexity upper-bound table；P1 quantified formula and non-vacuity condition；Discussion
- **Specific takeaway / limitation:** 已读摘要、四类问题定义、复杂度表、P1 公式与讨论。对固定点及最小 trap spaces 分别考虑全局或从指定源可达的标记重编程；永久干预允许创造和删除吸引子。局部单调情形的量词表达分别为 ∃∀ 与 ∃∀∃ 上界，不应将它们误报为文中已经证明的完备复杂度分类。P1 若不额外要求存在固定点，会被无固定点模型真空满足。研究计划中需要明确是否允许这种退化解。

### BIO127 · 2025 — Scalable Counting of Minimal Trap Spaces and Fixed Points in Boolean Networks

- **Author / form:** Kabir, Mohimenul; Trinh, Van-Giang; Pastva, Samuel; Meel, Kuldeep S · conference_paper
- **Theme / reading status:** `Boolean_network_theory` / `abstract_read`
- **Source:** https://doi.org/10.4230/LIPIcs.CP.2025.17
- **Actually inspected:** Abstract (complete, arXiv)
- **Specific takeaway / limitation:** 以近似 answer-set counting 计算最小 trap spaces 与固定点数量，避免逐个枚举，并在多种基准上比较表现。它处理给定网络的吸引子相关数量，不能直接代替跨规则族的精确极值证明；本次完整阅读摘要，未审计近似保证的全部推导。

### BIO128 · 2026 — A Boolean encoding of the Most Permissive semantics for Boolean networks

- **Author / form:** de Chancel, Laure; Mossé, Brigitte; Naldi, Aurélien; Remy, Élisabeth · preprint
- **Theme / reading status:** `Boolean_network_theory` / `fulltext_sections_read`
- **Source:** https://arxiv.org/abs/2604.03029
- **Actually inspected:** Abstract；Section 4 conclusion and outlook
- **Specific takeaway / limitation:** 已读摘要与 §4 结论。每个原变量用三个 Boolean 变量编码，所得异步模型精确重现原 MP 可达性；作者支持只展开部分变量以避免规模增长。讨论提出识别对语义差异关键的变量、比较随机模拟以及异步分步编码可能产生的概率伪影。可达性等价并不表示时间分布或转移概率等价。本次未逐行核查全部编码正确性证明。

### BIO129 · 2025 — An open problem: Why are motif-avoidant attractors so rare in asynchronous Boolean networks?

- **Author / form:** Samuel Pastva; Kyu Hyong Park; Ondřej Huvar; Jordan C. Rozum; Réka Albert · journal_paper
- **Theme / reading status:** `Boolean_network_theory` / `fulltext_sections_read`
- **Source:** https://doi.org/10.1007/s00285-025-02235-8
- **Actually inspected:** Abstract and introduction；Sections 7.4 and 9；Supplement A.1 general upper-bound construction and proof；Supplement A.2 Claims 1–5, root team reading；Supplement A.3 memory-state obstruction for cheaper alternative strategies
- **Specific takeaway / limitation:** 团队阅读正文 §7.4、§9 及补充材料 A.1–A.3。最小 trap spaces 与异步吸引子的一一对应可能失败；文中已有局部单调/nested canalizing 等简单排除条件不足的例子，均归于原作者。一般延迟上界 (N−d)(N−1)+m(m+1)/2 已在 A.1 证明：按变量最后一次 ON 的顺序选延迟，确保需要的记忆状态可达；星形族 floor(N²/4) 的最小值也已有证明。A.3 的可达性障碍针对尝试用更少延迟的替代策略，不是一般上界的缺口。作者未发现 m>1 时记忆不可达会使这些较便宜策略完全失败的实例；这一精确限定的判据或反例搜索可作为后续方向，不能把已证明的一般算法误称为条件性结果。

### BIO130 · 2025 — Refining Boolean models with the partial most permissive scheme

- **Author / form:** Ben Boina N; Mossé B; Baudot A; Remy E · journal_paper
- **Theme / reading status:** `Boolean_network_theory` / `fulltext_sections_read`
- **Source:** https://doi.org/10.1093/bioinformatics/btaf123
- **Actually inspected:** Complete abstract；Section 4 discussion and limitations
- **Specific takeaway / limitation:** MRBM 用部分 Most Permissive 语义识别需要多值化的变量，以恢复指定稳定态可达性。已读完整摘要与讨论：方法限制于无循环吸引子的动力学；自抑制变量不予多值化；参数化仍需穷举或个案推理。作者明确指出推广到循环吸引子不直接成立。

### BIO131 · 2023 — Models of Cell Processes are Far from the Edge of Chaos

- **Author / form:** Park KH; Costa FX; Rocha LM; Albert R; Rozum JC · journal_paper
- **Theme / reading status:** `Boolean_network_theory` / `fulltext_sections_read`
- **Source:** https://doi.org/10.1103/prxlife.1.023009
- **Actually inspected:** Complete abstract；Primary PMC introduction excerpts and discussion passages
- **Specific takeaway / limitation:** 对 72 个实证 Boolean 模型研究长期、允许相位差异的表型扰动响应，发现比短期 Derrida 指标所暗示的更强有序性。已读摘要与讨论相关段落。结论限定于功能模块，作者保留模块耦合后出现更大尺度临界行为的可能，并区分同步与异步更新。
