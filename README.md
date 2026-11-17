# Boolean GRN Extremal Combinatorics

A reproducible research workspace for extremal questions about **monotone Boolean gene regulatory networks** (GRNs), with an emphasis on rigorous, size-independent results rather than larger finite enumerations.

## Research target

The starting point is Section 6.3 and Algorithm 6.12 of:

B. V. Harshavardhan, S. Adigwe, M. K. Jolly, and T. Gedeon, [*Gene Regulatory Networks that Support Multi-fate Cellular Decisions*](https://doi.org/10.1007/s11538-026-01791-4), *Bulletin of Mathematical Biology* **88**, article 220 (2026). [Author code](https://github.com/Harshavardhan-BV/Monotone-Bool-Net).

Fix a fully connected signed network on `n` vertices, including a **positive self-loop** at each vertex. At a distinguished vertex, let exactly `m` of the other `n-1` incoming edges be inhibitory. After complementing those inhibitory inputs, define `W(n,m)` to be the set of increasing Boolean functions at that vertex which simultaneously support **all** single-high network states as fixed points. The primary extremal problem is

```text
K(n) = argmax_{0 <= m < n} |W(n,m)| .
```

The cited paper reports maximizing inhibitory counts `m=n-1` for `n=3,4`, but `m=1` for `n=5`; a general combinatorial explanation for `n>5` is open in that paper.

**Two distinct objectives must not be conflated:** (a) *equipotency*, where individual single-high states occur with equal frequency among compatible models (paper Section 5), and (b) *full multistability*, where one and the same model supports all these states (Section 6). This repository focuses on **(b)**. A previous six-node, no-self-loop network enumeration is a different setting and does not establish the `n>5` extremal result.

## Verified reference implementation

`scripts/count_full_multistability.py` uses exact bitset order-ideal counting on the Boolean lattice, with fixed-point constraints propagated by monotonicity. The test suite independently enumerates antichains (minimal true assignments) and checks the same counts. No external packages, GPU or wet-lab data are needed.

```sh
python3 scripts/count_full_multistability.py --max-n 5
python3 -m unittest discover -s tests -v
```

| Nodes `n` | Counts `|W(n,m)|` for `m=0,...,n-1` | Maximizing `m` |
| --- | --- | --- |
| 2 | 1, 4 | 1 |
| 3 | 2, 3, 10 | 2 |
| 4 | 9, 17, 14, 38 | 3 |
| 5 | 114, 575, 445, 148, 334 | 1 |

These are reproducible **finite checks**, not a new general theorem. The reference counter is deliberately bounded to `2 <= n <= 5`; its exponential strategy is unsuitable as an approach to arbitrary `n`.

## Research direction

See [RESEARCH.md](RESEARCH.md) for the mathematical work program and evidence standards. Priority is to replace repeated finite searches with a formula, recurrence, asymptotic result, rigorous extremal classification, or a decisive structural obstruction for unbounded `n`.

Any proposed theorem must list its precise assumptions and a proof. Computations should come with independently checkable scripts; claims about actual biological systems require biological evidence beyond this abstract network model.

## Status

Published repository, active research. The initial commit provides a faithful problem definition and checked small cases. **No claim of solving the open extremal problem is made.**

## Boundary asymptotics (research note)

[Boundary entropy and escape of optimal inhibitory degrees](notes/boundary_entropy.md)
proves fixed-boundary logarithmic asymptotics using the classical Dedekind
asymptotic. In particular, every sequence of maximizing degrees has both its
inhibitory and activating counts tending to infinity. This does **not** locate
the exact maximizer or show its ratio tends to one half. The extension proves
logarithmic exclusion bands for exact maximizers and characterizes first-order
optimal sequences; the latter result explains why leading entropy alone cannot
select a maximizing proportion. The note includes the
full proof, model scope, references and verification limits.

```sh
python3 scripts/boundary_bounds.py
python3 -m unittest discover -s tests -v
```

## Exact boundary and extended counts

[Exact slices and counts through seven nodes](notes/exact_slices.md) proves
`C(n,n-2)=D(n-1)-D(n-2)`, so this degree is never optimal, for any `n>=2`.
It also proves `C(n,n-3)>C(n,n-1)>C(n,n-2)` for every `n>=5`,
excluding both largest inhibitory degrees and showing the profile is not
unimodal. The exact six- and seven-node rows both have the unique maximizer `m=2`.
Six-node counts have a separate slice-enumeration check; seven-node counts
have two pivot-order checks and exact boundary identities. This does not
settle the general maximizing degree or its limiting proportion.

```sh
python3 scripts/count_full_multistability.py --max-n 7
python3 scripts/slice_counts.py
```
