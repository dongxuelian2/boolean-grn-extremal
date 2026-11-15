# Working proof: constant-width localization of inhibitory-degree maximizers

**Status:** candidate proof audited internally on 2026-11-15, **not** externally peer-reviewed, published, or established novel relative to all later literature. No effective threshold is claimed. See [roadmap](ROADMAP.md).

## Model

In the signed monotone GRN model of [RESEARCH.md](../../RESEARCH.md), there are \(n\) inputs including positive self-variable \(s\), \(m\) inhibitory other inputs \(Z\), and \(a=n-1-m\) activating other inputs \(A\). Complement inhibitory bits to make the local map increasing. The simultaneous single-high constraints are

\[
f(Z\cup\{s\})=1,\quad
f(Z\cup\{j\})=0\ (j\in A),\quad
f(Z\setminus\{j\})=0\ (j\in Z).
\]

Write \(C(n,m)\) for compatible maps, \(D(n)\) for all monotone \(n\)-bit maps, and \(K(n)=\arg\max_m C(n,m)\). Uniform monotone maps correspond to uniform antichains of minimal true assignments.

## Required external inputs

Jenssen, Malekshahian and Park, *On Dedekind's problem, a sparse version of Sperner's theorem, and antichains of a given size in the Boolean lattice*, [arXiv:2411.03400v2](https://arxiv.org/html/2411.03400v2), DOI [10.1112/jlms.70624](https://doi.org/10.1112/jlms.70624).

- Theorem 1.7: a uniform antichain is contained in ranks \(C_n=\bigcup_{r=\lfloor n/2\rfloor-1}^{\lceil n/2\rceil+1}L_r\), apart from probability \(\delta_n=\exp[-\Omega(n^2)]\).
- Section 5 and Lemma 6.1: a positive side-layer polymer representation with fair independent unblocked middle-layer choices for even \(n\).
- Corollary 7.10: odd \(n\) has two central phases, approximated in total variation with error \(\exp[-\Omega(n^2)]\).
- Eq. (4.4) and (3.6): the sum of weights of polymers containing a given side-layer site obeys a \(1/(2n^5)\) bound, with additional \(\exp[-\Omega(n^2)]\) penalty for components of size linear in \(n\).

These quantitative theorems are essential. A generic \(\log_2 D(n)\sim \binom n{\lfloor n/2\rfloor}\) estimate is insufficient for the rare constrained event.

## Central competitor has probability \(2^{-O(n)}\)

Let \(h=\lceil n/2\rceil\), \(m_0=h-1\), \(q=a+1=n-h+1\). Prescribe the value 1 at \(Z\cup\{s\}\) and 0 at \(Z\cup\{j\}\) for each \(j\in A\), a set \(T\subset L_h\) of \(q\) distinct vertices. In the corresponding central polymer phase, at most \(nq\) side-layer sites can block \(T\). Eq. (4.4) and union bound give probability at least \(1-q/(2n^4)\) of none blocking \(T\). Conditional on this, fair unblocked central bits realize the prescription with probability \(2^{-q}\). The inhibitory zeros of rank \(h-2\) are then automatic in this phase (and follow by monotonicity if \(a>0\)). In odd \(n\), take the phase centered at \(h\) with mixture weight one half. Subtract the exponentially smaller exceptional/TV probability. For all large \(n\),

\[
\frac{C(n,m_0)}{D(n)}\ge \frac14\,2^{-q}=2^{-O(n)}.
\]

## All but a constant-width band are exponentially rarer

Apply the central-layer theorem to the antichain of minimal true points of \(f\). Apply it separately to \(f^\dagger(x)=1-f(\mathbf1-x)\) to control maximal false points. Outside a set of probability \(2\delta_n\), every true point has rank at least \(\lfloor n/2\rfloor-1\), and every false point rank at most \(\lceil n/2\rceil+1\).

If \(m<\lfloor n/2\rfloor-2\), the specified true point at rank \(m+1\) violates the first condition. If \(m>\lceil n/2\rceil\) and \(a>0\), a specified activation-zero at rank \(m+1\) violates the second. When \(a=0\), inhibitory zeros at rank \(n-2\) exclude that endpoint for large \(n\). These candidates have relative count \(O(\delta_n)\), versus the central \(2^{-O(n)}\) lower bound. Therefore

\[
K(n)\subseteq[\lfloor n/2\rfloor-2,\lceil n/2\rceil]
\]

for all sufficiently large \(n\).

## Eliminate the right edge of that band

For even \(n=2k\), put \(m=k\). Dualize: specified activation zeros become \(k-1\) mandatory minimal true points \(v_j=\{s\}\cup(A\setminus\{j\})\), all of rank \(k-1\). They share the middle-layer upper neighbor \(\{s\}\cup A\), hence must occupy the same connected side-layer polymer of size at least \(k-1\). The cited polymer-weight bound gives this event probability \(\exp[-\Omega(n^2)]\), too small to maximize. For odd \(n=2k+1\), \(m=k+1\), the lower-centered phase has the same linear-size polymer obstruction; in the upper-centered phase the required lower-rank true points are impossible, apart from the known TV error. Thus the rightmost candidate is excluded.

The resulting **working theorem** is, for sufficiently large \(k\),

\[
\boxed{K(2k)\subseteq\{k-2,k-1\},\qquad K(2k+1)\subseteq\{k-2,k-1,k\}.}
\]

In particular, any sequence \(m_n\in K(n)\) has \(m_n/(n-1)\to1/2\).

## The remaining obstruction

The exact free-middle-rank formula in earlier draft PR #1 yields

\[
L(2k,k-2,k)=L(2k,k-1,k)=\binom{2k}k-(k+1).
\]

A naive central-layer comparison is therefore tied in even dimension. The unproved local-defect ratio heuristic is \(C(2k,k-1)/C(2k,k-2)=1+(k+1)2^{-k}+o(k2^{-k})\). For odd dimension the unproved two-phase heuristic gives leading candidate weights \(1:3:2\). Neither prediction is used in the preceding argument and both require independently controlled relative errors.

## Model boundary

For fixed graph \(G\) with inhibitory indegrees \(m_1,\ldots,m_n\), the full-network compatible count is exactly \(\prod_i C(n,m_i)\). This is insensitive to cycle and module placement at fixed degree sequence. Asymptotic localization therefore concerns degree balance within a stated Boolean-function ensemble; no biological prevalence or dynamical robustness follows.