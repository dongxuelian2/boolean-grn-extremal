# Research roadmap — 2026-11-15

## Mission and scope

Apply rigorous combinatorics to the **specific** extremal question in [Harshavardhan et al. (2026), §6.3](https://doi.org/10.1007/s11538-026-01791-4). The exact positive-self-loop, complete signed-input, simultaneous-single-high, redundant-inputs-allowed model is fixed in [RESEARCH.md](../../RESEARCH.md). Do not silently change network class or update semantics. The central question is \(K(n)=\arg\max_m C(n,m)\).

## Primary track A: asymptotic localization to exact classification

1. **Audit and formalize the central-window proof** in [central_window_working_proof.md](central_window_working_proof.md). Provisional conclusion for all sufficiently large \(k\):
   \(K(2k)\subseteq\{k-2,k-1\}\), \(K(2k+1)\subseteq\{k-2,k-1,k\}\). The argument uses quantitative central-layer/antichain results of Jenssen–Malekshahian–Park (DOI 10.1112/jlms.70624); check every transfer from typical antichains to constrained node maps and verify the error terms. This is a **working proof**, without effective \(n_0\) or exhaustive priority audit.
2. **Compare the remaining candidates at sufficient precision.** In even dimensions the free central-layer lower bound ties exactly:
   \(L(2k,k-2,k)=L(2k,k-1,k)=\binom{2k}{k}-(k+1)\). First-order Dedekind entropy and the central-layer lower bound cannot decide. Study the ratio \(C(2k,k-1)/C(2k,k-2)\), pinned polymer expansions, local defects and a uniform remainder smaller than the predicted gap.
3. **Analyze odd dimensions independently.** Two central phases contribute differently; rigorously compare \(m=k-2,k-1,k\). A heuristic leading ratio \(1:3:2\) remains unproved, and must not be promoted into a theorem.
4. **Close the finite gap.** Identify a computable/effective threshold, or prove an infinite-family classification and audit remaining finite exceptions with independent counting methods. A possible eventual unique-maximizer formula \(m=\lfloor n/2\rfloor-1\) is conjectural.

Acceptance: a precise stated theorem, complete proof with references and quantified errors, comparison to the original 2026 problem, independent checking, counterexample search, and a reviewable PR. More rows alone fail this criterion.

## Secondary track B: structural dynamical extensions (separate model)

The degree-count observable is exactly a product \(\prod_i C(n,m_i)\), hence cannot resolve cycles, modularity or reciprocal wiring at fixed indegrees. If biological structure beyond inhibitory counts is desired, replace the observable with one that depends on joint dynamics: asynchronous attractor reachability, perturbation robustness, or essential-variable restrictions. Specify update scheme and parameter ensemble first.

A distinct candidate concerns motif-avoidant attractors and delay placements in Pastva et al. (2025), DOI 10.1007/s00285-025-02235-8. Its known sharp delay-count bound is **not** new. The [delay note](async_delay_notes.md) derives a necessary degree multiset for optimizers, while edge placement and reachability remain open within the defined star example. Its update functions differ from the signed-monotone GRN class above: never transfer conclusions between them without a reduction.

## Evidence and literature workflow

- Read [claim register](CLAIM_REGISTER.md) before citing results. Mark as published, prior-work reproduced, proof-audited working result, experimentally checked, conjectural, or open.
- Use [131-record reading ledger](../literature/reading-ledger-2026-11-15.md); 102 entries document abstract/sections/proof reading and 29 are bibliography-only. This is not a claim that 131 entire papers were read.
- For each candidate publish source DOI, section/page, precise assumptions, proof status, counterexample attempts, novelty check, and machine-reproducible commands. Favor relevant original and later citing papers.
- Prioritize proof quality over counting throughput. Stop a path that repeatedly adds finite tables without an explicit unbounded-\(n\) mechanism.

## Sequence

**M1** central-window proof review and explicit use of external lemmas → **M2** even/odd refined candidate comparison → **M3** effective threshold or infinite-family classification → **M4** separately validated dynamical/biological extension. Existing [PR #1](https://github.com/dongxuelian2/boolean-grn-extremal/pull/1) remains a separate foundational draft.