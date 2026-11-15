"""Independent self-coordinate slice enumeration, deliberately limited to n<=6.

Truth tables use bit x for input x. Construct MBFs as ordered pairs of lower-
and upper-coordinate slices, rather than by forced-point deletion.
"""
from functools import lru_cache


@lru_cache(None)
def monotone_tables(d):
    if not 0 <= d <= 5:
        raise ValueError('table generation is limited to 0 <= d <= 5')
    if d == 0:
        return (0, 1)
    tables = monotone_tables(d - 1)
    shift = 1 << (d - 1)
    return tuple(g | (h << shift) for g in tables for h in tables if g & ~h == 0)


def slice_row(n):
    if not 2 <= n <= 6:
        raise ValueError('slice verification is limited to 2 <= n <= 6')
    tables = monotone_tables(n - 1)
    counts = []
    for m in range(n):
        neg = (1 << m) - 1
        zeros = sum(1 << (neg ^ (1 << j)) for j in range(n - 1))
        lower = [g for g in tables if g & zeros == 0]
        upper = [h for h in tables if (h >> neg) & 1]
        counts.append(sum(g & ~h == 0 for g in lower for h in upper))
    return counts


if __name__ == '__main__':
    for n in range(2, 7):
        print(n, slice_row(n))


def two_activator_counts(m):
    """Return (a=2, a=1, a=0) at n=m+3 via the MBF(m) lattice.

Independent exact weighted-interval identities; limited to m<=4 to keep
interval enumeration small. This routine does not call the poset counter.
"""
    if not 0 <= m <= 4:
        raise ValueError('weighted interval verification requires 0 <= m <= 4')
    lattice = monotone_tables(m)
    a2 = a1 = dedekind_next2 = 0
    for v in lattice:
        ideal = [u for u in lattice if u & ~v == 0]
        p = len(ideal)
        t = sum(sum(u & ~w == 0 for w in ideal) ** 2 for u in ideal if u != 0)
        a2 += p * t
        a1 += t + p * (p - 1)
        dedekind_next2 += t + p*p
    return a2, a1, 2 * (dedekind_next2 - 1)
