# Boundary entropy and escape of optimal inhibitory degrees

## Statement

Let C(n,m) have exactly the meaning fixed in RESEARCH.md: every node has a positive self-loop, m of the other n−1 inputs are inhibitory, redundant inputs are permitted, and all single-high states must be fixed **simultaneously**. Put a=n−1−m and b_n=binom(n,floor(n/2)). Let D(d) count all increasing Boolean functions on d variables, including constants.

**Theorem.** In this model:

1. For each fixed integer m≥0,
   log₂ C(n,m) / b_n → 1−2^(−m−1).
2. For each fixed integer a≥0,
   log₂ C(n,n−1−a) / b_n → 1−(a+1)2^(−a−1).
3. log₂ max_m C(n,m) / b_n → 1.
4. For every fixed K, all maximizers eventually satisfy K<m<n−1−K. In particular, along any sequence of maximizers, both inhibitory and activating input counts tend to infinity.

Parts 1–2 concern fixed boundary parameters only, not a uniform expansion for varying m. Part 4 gives neither an effective threshold nor m/n→1/2. It does not identify K(n) exactly. These are proposed deductions for the specified extremal problem, not a claim that its complete solution or publication novelty has been established.

## Free vertices and antichain lower bounds

Write a Boolean assignment as (s,z,y), with self-coordinate s, inhibitory coordinates z⊆Z, |Z|=m, and activating coordinates y⊆A, |A|=a. Complementing inhibitory inputs converts the node map to an increasing function. The required true vertex is (1,Z,∅). Required false vertices are (0,Z\{j},∅) for j∈Z and (0,Z,{j}) for j∈A.

When a≥1, upward/downward propagation therefore forces

- value 1 precisely on s=1, z=Z;
- value 0 precisely on s=0, |y|≤1.

Here “precisely” refers to forced values from these constraints; other values may also equal zero or one in particular functions. The two sets are disjoint. When a=0, the forced-zero set is instead s=0, z⊊Z; the forced-one set consists of the top vertex.

Use binom(d,k)=0 outside 0≤k≤d. The number of free vertices of rank r, for a≥1, is

    L(n,m,r) = binom(n,r) − binom(a,r−m−1)
                            − binom(m,r) − a binom(m,r−1).       (1)

For a=0 replace the last two terms by binom(m,r) if r<m, and by zero otherwise.

For any subset T of free rank-r vertices, declare true the upward closure of T together with the forced-one set. This does not meet the forced-zero down-set. Distinct subsets give distinct values on that rank, because its vertices form an antichain and are not forced true. Consequently

    2^L(n,m,r) ≤ C(n,m) ≤ D(n).                                (2)

This extends arbitrary same-rank choices; it does not count free vertices as independent across different ranks.

## Slice upper bounds

Fix (s,z) and vary y. Each restriction is an increasing function on a variables. The slice s=1,z=Z is identically one. Forgetting all compatibility constraints between the remaining slices gives the injective encoding bound

    C(n,m) ≤ D(a)^(2^(m+1)−1).                                (3)

Alternatively, fix (s,y) and vary z. If a≥1, the a+1 slices with s=0 and |y|≤1 are identically zero. Thus

    C(n,m) ≤ D(m)^(2^(a+1)−a−1),       a≥1.                   (4)

These bounds need not be sharp at finite n. They count tuples of monotone restrictions that include tuples not satisfying cross-slice compatibility, which is legitimate for an upper bound.

For a=0 there is an exact identity:

    C(n,n−1) = 2(D(n−1)−1).                                   (5)

Indeed, the upper self-slice is any monotone map taking value one at its top (all maps except constant zero), while the lower slice is zero off its top and has an independent choice at that top. The only cross-slice inequality involving a possibly true lower value is satisfied by the fixed upper top.

## Asymptotic proof

The only external enumerative input is the classical Dedekind logarithmic asymptotic

    log₂ D(d) = (1+o(1)) binom(d,floor(d/2)).                   (6)

It is due to Kleitman [2]; an accessible independent entropy proof is Pippenger [3, Theorem 2.1]. For fixed h and a fixed bounded displacement of the central rank,

    binom(n−h,floor(n/2)+O(1)) / b_n → 2^(−h).                (7)

This follows directly from the factorial ratio (with parity treated on the two subsequences).

For fixed m, eventually r=floor(n/2)>m+1. Both forced-zero terms in (1) vanish, so (1), (2), and (7) give the lower coefficient 1−2^(−m−1). The upper bound (3), (6), and b_(n−m−1)/b_n→2^(−m−1) give the same coefficient. This proves part 1, including m=0.

For fixed a≥1, eventually r<m+1, so the forced-one term vanishes. Equations (1), (2), and (7) give lower coefficient 1−(a+1)2^(−a−1). Equations (4) and (6) match it from above. When a=0, (5) and (6) give coefficient 1/2, exactly the stated formula. This proves part 2.

For part 3 choose m=r=floor(n/2), so a=n−1−r≥1 for n≥4. Formula (1) simplifies to

    L(n,r,r) = b_n − 1 − ar.                                  (8)

No rank-r vertex is forced true; the forced-zero vertices are Z itself and the ar sets obtained by removing one inhibitory coordinate and adding one activating coordinate. Since ar=O(n²)=o(b_n), (2), (6), and (8) prove part 3.

Finally, for fixed K, parts 1–2 supply finitely many boundary limits, each strictly less than one. Part 3 supplies a comparison value with limit one. For all sufficiently large n every m≤K or a≤K is therefore strictly suboptimal. This proves part 4 without interchanging a nonuniform limit over an unbounded set of m. ∎

## Verification and scope

`scripts/boundary_bounds.py` implements the exact rank formula and lower bounds using integer arithmetic; it does not attempt exponential enumeration for arbitrary n. The new tests compare every rank for all n≤10 against independently propagated signed-state constraints; compare bounds to the existing exact counts for n≤5; and check (8) through n=100. The original independent-antichain baseline remains unchanged. Computation checks the finite combinatorial identities; the asymptotic conclusions follow from the proof, not extrapolation of a table.

An independent proof review checked the free-layer extension, exceptional a=0 case, slice encoding, fixed-boundary matching asymptotics, and the finite-union quantifier in part 4.

We inspected the source paper's Section 6.3 and Algorithm 6.12, and the author implementation at commit `964b78a67932a1ea369034a936d7e70a4816e254`, especially `SinglePositive/ms_count.py` and `src/mbnet/tl.py::unconstrained_count`. A direct execution of the author package was attempted but its `networkx` dependency was unavailable; we do not claim an executed author-code reproduction. The existing two independent baseline implementations were executed successfully. The author code propagates constraints and recursively counts unconstrained assignments; this note does not claim that routine as a new algorithm. The earlier balanced-network paper [4] treats related prevalence questions in a different network class. We have not established exhaustive novelty against the full constrained-antichain literature.

The earlier no-self-loop equipotency enumeration is not used here. This theorem concerns a specified combinatorial ensemble, not observed biological probabilities. A useful next target would be a **quantitative growing boundary exclusion** or sharper uniform bounds that distinguish interior candidates; exact K(n) and the growth rates of its elements remain open in this note.

## References

1. B. V. Harshavardhan, S. Adigwe, M. K. Jolly and T. Gedeon. *Gene Regulatory Networks that Support Multi-fate Cellular Decisions*. Bulletin of Mathematical Biology 88, 220 (2026). https://doi.org/10.1007/s11538-026-01791-4 . Author code: https://github.com/Harshavardhan-BV/Monotone-Bool-Net .
2. D. Kleitman. *On Dedekind's problem: the number of monotone Boolean functions*. Proceedings of the American Mathematical Society 21 (1969), 677–682. https://doi.org/10.1090/S0002-9939-1969-0241334-6 .
3. N. Pippenger. *Entropy and Enumeration*. University of British Columbia technical report TR-98-02 (1998), Theorem 2.1. https://www.cs.ubc.ca/sites/default/files/tr/1998/TR-98-02_0.pdf . This source was accessible and explicitly proves the asymptotic used in (6); the AMS PDF endpoint returned HTTP 403 during this review.
4. S. Adigwe, Harshavardhan BV, M. K. Jolly and T. Gedeon. *Characterization of monotone Boolean models supporting fixed points and multistability in balanced networks*. PLOS Complex Systems 3(5), e0000103 (2026). https://doi.org/10.1371/journal.pcsy.0000103 .
