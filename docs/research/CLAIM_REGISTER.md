# Claim register (2026-11-15)

| Claim | State | Evidence and next requirement |
| --- | --- | --- |
| Eventual classification, manuscript version | **independent model-agent and integration review passed** | [Paper](../../manuscript/main.tex), [review](independent-grn-review-2026-11-15.md); not external human peer review |
| Explicit local cutoff `2^20` and remainder `2^24 n^300 2^-n` | **conditional finite theorem** | Requires source KP; full certificate also requires TV <=`2^-2n`. No numerical unconditional global cutoff is proved. |
| Simultaneous single-high positive-self-loop model | source-defined | [Harshavardhan et al., §6.3](https://doi.org/10.1007/s11538-026-01791-4); [RESEARCH.md](../../RESEARCH.md) |
| Exact \(n=2,\dots,5\) values | independently finite-checked | Main scripts and antichain tests; **no universal extrapolation** |
| Boundary entropy / logarithmic degree exclusions | mathematically argued, draft PR | [PR #1](https://github.com/dongxuelian2/boolean-grn-extremal/pull/1); audit Kleitman–Markowsky assumptions and external constants |
| \(C(n,n-3)>C(n,n-1)>C(n,n-2)\) for \(n\ge5\) | proof in draft PR | [Exact-slices note at PR head](https://github.com/dongxuelian2/boolean-grn-extremal/blob/research/boundary-entropy/notes/exact_slices.md); verify proof/CI separately |
| Central-width asymptotic localization \(K(2k)\subseteq\{k-2,k-1\}\), \(K(2k+1)\subseteq\{k-2,k-1,k\}\) | **working proof, not yet peer reviewed** | [Proof](central_window_working_proof.md); re-check external antichain theorem and quantitative bounds, seek independent proof reviewer |
| Even ratio `1+(k+1)2^-k+O(k^1000 2^-2k)` and odd weights `1:3:2` | **complete proof draft, external review outstanding** | [Localized KP and rooted-polymer proof](eventual_extremal_classification.md); finite shadow/coefficient audit in `scripts/check_local_coefficients.py` |
| Eventual unique maximizer `K(n)={floor(n/2)-1}` | **new theorem proof draft, not peer reviewed** | Same note combines parity comparisons with rechecked localization; no explicit unconditional numerical cutoff; broader priority review open |
| Full-network count depends only on inhibitory indegrees | exact elementary factorization under fixed model | \(\prod_i C(n,m_i)\); does **not** identify topology, biological probability, or dynamical robustness |
| Optimal star-delay degree multiset | derived necessary condition in separate async model | [Delay note](async_delay_notes.md); based on established sharp bound of Pastva et al.; not sufficient for edge placement |
| All-\(n\) \(K(n)\) and empirical cellular interpretation | **open** | No exact classification or biological validation |

**Novelty discipline:** A valid proof and a novel publishable result are separate questions. Keep sources and source versions. The 2026 primary paper's specific extremal problem is recent, although Boolean networks and the underlying combinatorics have a long history.
