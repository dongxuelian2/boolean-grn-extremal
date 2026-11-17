# Boolean GRN Extremal Combinatorics

This project studies the inhibitory input counts that maximize full
single-high multistability in signed monotone Boolean gene-regulatory networks.

## Model and results

Consider a complete signed network on `n` vertices with a positive self-loop
at every vertex. At a distinguished node, exactly `m` of the other `n − 1`
inputs are inhibitory. Local rules respect the input signs and may have
redundant variables. Every single-high state must be fixed by the same network.
After complementing inhibitory coordinates, let `C(n,m)` count the compatible
monotone local rules, and define

```text
K(n) = argmax_{0 ≤ m < n} C(n,m).
```

The manuscript gives an argument that `K(n) = {floor(n/2) − 1}` for all
sufficiently large `n`. Its even and odd cases use local polymer estimates and
antichain concentration. A finite certificate for `n ≥ 2^20` assumes the
specified Kotecký–Preiss inequality and phase-approximation bound at the
relevant dimension. An unconditional numerical cutoff and a classification
for every finite size remain open. External peer review and broader priority
review are pending.

For a fixed signed graph with inhibitory indegrees `m_i`, the network count
factors as `∏ C(n,m_i)`. The results describe this combinatorial count;
attractor basins and biological probabilities require separate models and
measurements.

The model follows Section 6.3 and Algorithm 6.12 of [Harshavardhan et al.
(2026)](https://doi.org/10.1007/s11538-026-01791-4). The paper also studies
single-state equipotency, a different observable.

- [Manuscript](manuscript/main.tex): eventual classification, assumptions,
  proof, and references.
- [Eventual classification note](docs/research/eventual_extremal_classification.md):
  local estimates, asymptotics, and the conditional finite certificate.
- [Research model](RESEARCH.md): definitions and fixed-point constraints.
- [Claim register](docs/research/CLAIM_REGISTER.md): evidence and open questions.
- [Research roadmap](docs/research/ROADMAP.md): further mathematical targets.
- [Literature ledger](docs/literature/reading-ledger-2026-11-15.md): sources
  and their inspection levels.

## Reproduce

The baseline enumerator uses Python's standard library. Its small-case counts
are checked independently by antichain enumeration:

```sh
python3 scripts/count_full_multistability.py --max-n 5
python3 -m unittest discover -s tests -v
```

| `n` | `C(n,0), …, C(n,n−1)` | Maximizing `m` |
| --- | --- | --- |
| 2 | 1, 4 | 1 |
| 3 | 2, 3, 10 | 2 |
| 4 | 9, 17, 14, 38 | 3 |
| 5 | 114, 575, 445, 148, 334 | 1 |

Run `python3 scripts/check_grn_local_threshold.py` for the elementary
finite-certificate calculations and `python3 scripts/check_local_coefficients.py`
for the shadow and algebra checks. These finite checks accompany the proof.

Build the manuscript with `bash scripts/build_manuscript.sh` and a LaTeX
installation. With Pandoc and XeLaTeX, `bash scripts/build_proof_pdf.sh`
renders the classification note.
