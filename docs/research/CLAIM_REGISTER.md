# Claim register (2026-11-15)

| Claim | State | Evidence and next requirement |
| --- | --- | --- |
| Simultaneous single-high positive-self-loop model | source-defined | [Harshavardhan et al., §6.3](https://doi.org/10.1007/s11538-026-01791-4); [RESEARCH.md](../../RESEARCH.md) |
| Exact \(n=2,\dots,5\) values | independently finite-checked | Main scripts and antichain tests; **no universal extrapolation** |
| Boundary entropy / logarithmic degree exclusions | mathematically argued, draft PR | [PR #1](https://github.com/dongxuelian2/boolean-grn-extremal/pull/1); audit Kleitman–Markowsky assumptions and external constants |
| \(C(n,n-3)>C(n,n-1)>C(n,n-2)\) for \(n\ge5\) | proof in draft PR | [Exact-slices note at PR head](https://github.com/dongxuelian2/boolean-grn-extremal/blob/research/boundary-entropy/notes/exact_slices.md); verify proof/CI separately |
| Central-width asymptotic localization \(K(2k)\subseteq\{k-2,k-1\}\), \(K(2k+1)\subseteq\{k-2,k-1,k\}\) | **working proof, not yet peer reviewed** | [Proof](central_window_working_proof.md); re-check external antichain theorem and quantitative bounds, seek independent proof reviewer |
| Even/odd local ratios and eventual uniqueness | **conjectural/heuristic** | Need pinned cluster expansion, remainder control, finite exceptions |
| Full-network count depends only on inhibitory indegrees | exact elementary factorization under fixed model | \(\prod_i C(n,m_i)\); does **not** identify topology, biological probability, or dynamical robustness |
| Optimal star-delay degree multiset | derived necessary condition in separate async model | [Delay note](async_delay_notes.md); based on established sharp bound of Pastva et al.; not sufficient for edge placement |
| All-\(n\) \(K(n)\) and empirical cellular interpretation | **open** | No exact classification or biological validation |

**Novelty discipline:** A valid proof and a novel publishable result are separate questions. Keep sources and source versions. The 2026 primary paper's specific extremal problem is recent, although Boolean networks and the underlying combinatorics have a long history.