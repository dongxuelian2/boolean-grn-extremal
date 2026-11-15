# Research program

## Current active theorem program (2026-11-15)

The long-term problem statement below remains binding, but the current research order and result status are in [docs/research/ROADMAP.md](docs/research/ROADMAP.md), [the claim register](docs/research/CLAIM_REGISTER.md), and [umbrella Issue #3](https://github.com/dongxuelian2/boolean-grn-extremal/issues/3). In particular, the central-width result is a working proof awaiting further review; neither a global finite-n classification nor biological causal claims are established.

The [new eventual-classification proof draft](docs/research/eventual_extremal_classification.md)
now resolves the remaining asymptotic candidate comparison. Its local KP
perturbation lemma and the resulting eventual unique maximizer await external
review. The finite threshold and all-size classification remain open.


## Problem and source

Primary source: Harshavardhan, Adigwe, Jolly and Gedeon (2026), DOI: https://doi.org/10.1007/s11538-026-01791-4 — especially Sections 5, 6.1, 6.3 and Algorithm 6.12. Inspect the [authors' reference implementation](https://github.com/Harshavardhan-BV/Monotone-Bool-Net) before claiming a new counting algorithm.

### Fixed mathematical model

- Network: all-to-all directed graph on n vertices with positive self-activation at every vertex.
- At node i, m incoming interactions from other vertices are inhibitory; the others are activating.
- Each compatible node update function is monotone with the appropriate input signs. Redundant variables are allowed under the paper's convention.
- The target states are all unit vectors e_1, ..., e_n, **simultaneously** fixed by a single Boolean network.

For one node, complement the inhibitory input coordinates to obtain an increasing Boolean function f on the Boolean lattice B_n. Write Z for the set of m inhibitory other-node inputs and beta_Z(x)=x XOR Z (bitwise). Then f must satisfy

    f(beta_Z(e_i)) = 1,
    f(beta_Z(e_j)) = 0 for j != i.

Define C(n,m) as the number of increasing functions satisfying these simultaneous constraints. The extremal set of inhibitory degrees is

    K(n) = {m in {0,...,n-1}: C(n,m)=max_k C(n,k)}.

The optimization here is **not** the distinct "equipotency" problem of Section 5, and is not equivalent to counting networks up to graph isomorphism. For a fully connected fixed signed network with all positive self-loops, its admissible node maps can be chosen independently, giving a product of node-level counts.

## Priority theorem target

Find a size-independent statement characterizing K(n), or proving useful asymptotic or rigorous bounds on C(n,m). The small-n change of optimal m should be explained structurally, not merely tabulated at larger n.

This is a **research question**, not a conjecture already known to be true. Compute and inspect additional examples to *test* any candidate theorem; do not extrapolate a universal law from n<=5.

Suggested proof routes to evaluate against prior work:

1. Express C(n,m) as the number of upsets of a Boolean-lattice induced poset with forced upper/lower sets. Identify a canonical poset and seek structural reduction, transfer/recurrence, or injections between nearby m.
2. Look for symmetries, order-preserving embeddings, log-concavity/unimodality counterexamples, and comparison inequalities between m cases.
3. Compare the paper's Algorithm 6.12 against independently written counting code. Study antichain / Dedekind-number literature before claiming new formulas.
4. If an exact general maximizer is inaccessible, target a provable nontrivial infinite family, sharp asymptotic, or a structural impossibility result that directly narrows the published open problem.

## First substantive PR

A good first research PR should include a precise, independently checked mathematical claim: e.g. a new recurrence plus proof, a nontrivial general inequality, or an infinite family theorem. Extra isolated n values may support a theorem but do not replace one. Cite which statements are already in the 2026 paper.

The initial small-n baseline is already checked with two different enumeration methods. Do not resubmit the same calculations as a discovery.

## Practical constraints

No wet lab; use public literature and mathematically specified models. Available local machine: Ryzen 7 7840H, 32 GB RAM, RTX 4060 Laptop 8 GB. Favor portable Python and standard Linux shell commands; avoid expensive cloud requirements. Do not infer experimentally observed biological causal relations from Boolean-network combinatorics alone.

Proof statements, scripts and figures should be independently auditable. Stop or redirect a line of attack if it repeatedly produces only finite-case data without a credible route to a general result. This priority is about maximizing probability of an important **valid** result, not overstating novelty or reducing verification.
