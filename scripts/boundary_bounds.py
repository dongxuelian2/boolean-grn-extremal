"""Exact rank bounds for Section 6.3's positive-self-loop model.

This evaluates combinatorial formulas, not unrestricted Dedekind numbers.
"""
from math import comb
from fractions import Fraction


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def free_rank(n, m, rank):
    """Number of unconstrained rank-rank vertices of B_n."""
    if n < 2 or not 0 <= m < n or not 0 <= rank <= n:
        raise ValueError("require n>=2, 0<=m<n and 0<=rank<=n")
    a = n - 1 - m
    ones = choose(a, rank - m - 1)
    if a:
        zeros = choose(m, rank) + a * choose(m, rank - 1)
    else:
        zeros = choose(m, rank) if rank < m else 0
    return choose(n, rank) - ones - zeros


def lower_log2(n, m):
    """Exact integer L with C(n,m)>=2**L, using the best rank."""
    return max(free_rank(n, m, r) for r in range(n + 1))


def inhibitory_boundary_coefficient(m):
    if m < 0:
        raise ValueError("m must be nonnegative")
    return 1 - Fraction(1, 2 ** (m + 1))


def activating_boundary_coefficient(a):
    if a < 0:
        raise ValueError("a must be nonnegative")
    return 1 - Fraction(a + 1, 2 ** (a + 1))


if __name__ == '__main__':
    for n in (4, 5, 10, 20, 50, 100):
        m = n // 2
        central = choose(n, n // 2)
        L = free_rank(n, m, n // 2)
        print(f'n={n}, m={m}, central={central}, lower_log2={L}, relative_deficit={Fraction(central-L,central)}')
