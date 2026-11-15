# Boolean GRN Extremal Combinatorics

A theorem-first research project on **full simultaneous single-high multistability** in signed monotone Boolean gene-regulatory networks. Our principal objective is a structural characterization of the maximizing number of inhibitory inputs for arbitrary network size—not further isolated counting rows.

## Precisely defined problem

A complete signed network has \(n\) vertices, a **positive self-loop** at each vertex, and \(m\) inhibitory inputs among the other \(n-1\) inputs of a distinguished node. Each local rule respects the signs (redundant variables are permitted). All \(n\) single-high states \(e_1,\ldots,e_n\) must be fixed by the **same** Boolean network. After complementing inhibitory coordinates, let \(C(n,m)\) count admissible monotone local functions. We seek

\[
K(n)=\operatorname*{arg\,max}_{0\le m<n}C(n,m).
\]

This follows Section 6.3 and Algorithm 6.12 of [Harshavardhan et al. (2026)](https://doi.org/10.1007/s11538-026-01791-4). Do not conflate this with single-state equipotency or with an earlier no-self-loop enumeration.

**Active research tracker:** [Issue #3 — inhibitory-degree classification](https://github.com/dongxuelian2/boolean-grn-extremal/issues/3). Detailed documentation changes are in [draft PR #2](https://github.com/dongxuelian2/boolean-grn-extremal/pull/2).

**New proof draft (2026-11-15):** [eventual unique extremum](docs/research/eventual_extremal_classification.md).
A local polymer perturbation argument gives `K(n)={floor(n/2)-1}` for all
sufficiently large `n`, resolving both parity cases. The even ratio has positive
correction `(k+1)2^-k`, and odd candidate weights are asymptotically `1:3:2`.
The proof awaits external review; no effective threshold or all-size classification is claimed.

Run `python scripts/check_local_coefficients.py` for the finite shadow/algebra
audit. With Pandoc and XeLaTeX installed, `bash scripts/build_proof_pdf.sh`
renders the complete proof note to `output/pdf/`.

## Start here

| Resource | Purpose |
| --- | --- |
| [RESEARCH.md](RESEARCH.md) | Exact mathematical model, original problem, source and reproducibility constraints |
| [Research roadmap](docs/research/ROADMAP.md) | Prioritized theorem targets, alternative tracks, milestones, stop criteria |
| [Claim register](docs/research/CLAIM_REGISTER.md) | Published / existing / working / open claims and validation responsibilities |
| [Central-window working proof](docs/research/central_window_working_proof.md) | Candidate proof using quantitative antichain concentration; **not yet peer reviewed** |
| [Eventual classification proof](docs/research/eventual_extremal_classification.md) | Localized remainder estimates, even tie-breaking, odd phase comparison; **proof draft** |
| [Async-delay structural note](docs/research/async_delay_notes.md) | Separate model: a necessary degree profile for optimal delay placements |
| [Literature reading ledger](docs/literature/reading-ledger-2026-11-15.md) | 131 deduplicated scholarly works, each with source, actual reading status and specific note |
| [Earlier exact/asymptotic draft PR #1](https://github.com/dongxuelian2/boolean-grn-extremal/pull/1) | Boundary entropy, exclusion, exact slices, tests; **not yet merged** |

The original reference implementation remains in scripts/ and tests/. On main the reproducible small-case baseline is \(n\le 5\), while the draft PR additionally computes \(n=6,7\) and proves nontrivial boundary exclusions.

## Run the existing baseline

~~~sh
python3 scripts/count_full_multistability.py --max-n 5
python3 -m unittest discover -s tests -v
~~~

Validated main-branch counts:

| \(n\) | \(C(n,0),\ldots,C(n,n-1)\) | maximizer |
| --- | --- | --- |
| 2 | 1, 4 | 1 |
| 3 | 2, 3, 10 | 2 |
| 4 | 9, 17, 14, 38 | 3 |
| 5 | 114, 575, 445, 148, 334 | 1 |

## What is and is not a result

Draft PR #1 proposes rigorous boundary results, including \(C(n,n-3)>C(n,n-1)>C(n,n-2)\) for all \(n\ge5\); the exact all-size maximizer remains open. A later working proof narrows the asymptotic candidates to a constant-width central window but has not established eventual uniqueness or an effective threshold. These findings concern **counts under the defined combinatorial ensemble**. For a fixed signed graph \(G\) with inhibitory indegrees \(m_i\), its admissible full-network count factors as \(\prod_i C(n,m_i)\), so this observable cannot distinguish distinct cycle architectures having identical indegrees. Claims about real-cell probabilities, attractor basins or causal regulatory mechanisms require separate dynamical and biological validation.

See the [roadmap](docs/research/ROADMAP.md) before opening a new research branch. Proof, source-version audit and independent checks are required before calling an assertion established.
