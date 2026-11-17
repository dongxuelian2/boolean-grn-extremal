# Mathematical model

The problem follows Sections 5 and 6 and Algorithm 6.12 of
[Harshavardhan et al. (2026)](https://doi.org/10.1007/s11538-026-01791-4).
The [authors' implementation](https://github.com/Harshavardhan-BV/Monotone-Bool-Net)
provides a reference for the published counting procedure.

Consider the complete directed network on `n` vertices with a positive
self-loop at each vertex. At a fixed vertex `i`, let `Z` be the set of `m`
inhibitory inputs from other vertices; all remaining inputs activate. A local
update rule is monotone in each input according to its sign, and may have
redundant variables. The target states are the `n` unit vectors, all fixed
simultaneously by one network.

Complement the coordinates in `Z` and write `β_Z(x) = x XOR Z`. The resulting
local rule is increasing on the Boolean lattice and must satisfy

```text
f(β_Z(e_i)) = 1,
f(β_Z(e_j)) = 0  for j ≠ i.
```

Let `C(n,m)` count such increasing functions. The choice of which `m`
other coordinates are inhibitory is immaterial by permutation symmetry.
The extremal degree set is

```text
K(n) = {m in {0, ..., n − 1}: C(n,m) = max_k C(n,k)}.
```

For a fixed signed graph with inhibitory indegrees `m_i`, the local choices
are independent. The number of compatible networks is therefore
`∏_i C(n,m_i)`. This objective describes simultaneous fixed states; the
source's equipotency question considers the occurrence of individual states.
The network count also differs from a count up to graph isomorphism.

The [manuscript](manuscript/main.tex) develops the eventual classification and
its conditional finite certificate. The [claim register](docs/research/CLAIM_REGISTER.md)
records their evidence and review status; the [roadmap](docs/research/ROADMAP.md)
records the remaining mathematical questions.
