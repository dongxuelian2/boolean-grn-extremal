# Research roadmap

The [mathematical model](../../RESEARCH.md) fixes the signed-input network and
counting observable. The [manuscript](../../manuscript/main.tex) gives an
argument for the eventual unique maximizer, a local remainder, and a finite
certificate conditional on explicit source inequalities. The
[claim register](CLAIM_REGISTER.md) records the status and evidence for each
result.

## Eventual classification

The immediate proof-review tasks are to check the localized
Kotecký–Preiss perturbation and rooted-polymer estimates, the suppressed odd
phase, and the exclusion of the remaining degree candidates. These arguments
use quantitative antichain concentration from Jenssen, Malekshahian, and
Park, DOI 10.1112/jlms.70624. Finite coefficient checks support the algebra;
the asymptotic argument requires its cited estimates and the stated proofs.

The even comparison needs the first nonzero correction: the central-layer
leading terms tie for `m = k − 2` and `m = k − 1`. The odd comparison uses
the two central phases and the leading weights `1:3:2`. The
[classification note](eventual_extremal_classification.md) gives these
calculations; the [central-window note](central_window_working_proof.md)
records the localization argument.

## Finite sizes and prior work

Extract an unconditional numerical threshold from the source inequalities,
then resolve the remaining finite range with independently checkable counting
or structural comparisons. A direct all-size comparison would also address
this target. The [boundary results PR](https://github.com/dongxuelian2/boolean-grn-extremal/pull/1)
contains separate degree exclusions and exact slices that need comparison
with the manuscript and prior literature. The [literature ledger](../literature/reading-ledger-2026-11-15.md)
records which sources were inspected and at what depth; broader priority
review remains open.

## Separate dynamical model

The fixed-graph network count factors by inhibitory indegree. Questions about
cycle structure, perturbation robustness, or attractor reachability require a
model of joint dynamics and an explicit update scheme. The
[delay note](async_delay_notes.md) examines a separate asynchronous model:
it derives a necessary degree multiset for optimal star-delay placements,
while edge placement and reachability remain open.
