"""Independent antichain enumeration of all increasing Boolean functions."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from count_full_multistability import count_models, row


def antichains(n: int):
    """Generate antichains in the Boolean lattice without monotone-function DP."""
    points = tuple(range(1 << n))
    comparable = {x: {y for y in points if (x & y) in (x, y)} for x in points}

    def walk(candidates: tuple[int, ...], chosen: tuple[int, ...]):
        if not candidates:
            yield chosen
            return
        x = candidates[0]
        yield from walk(candidates[1:], chosen)
        yield from walk(tuple(y for y in candidates[1:] if y not in comparable[x]), chosen + (x,))

    yield from walk(points, ())


def independent_row(n: int):
    counts = [0] * n
    total = 0
    for minimal_true in antichains(n):
        total += 1
        for m in range(n):
            neg = sum(1 << j for j in range(1, m + 1))

            def value(x):
                return any((a & x) == a for a in minimal_true)

            if value(neg | 1) and all(not value(neg ^ (1 << j)) for j in range(1, n)):
                counts[m] += 1
    return total, counts


class ExactCounts(unittest.TestCase):
    def test_small_rows_independent(self):
        dedekind = {2: 6, 3: 20, 4: 168, 5: 7581}
        for n, expected_total in dedekind.items():
            with self.subTest(n=n):
                total, reference = independent_row(n)
                self.assertEqual(total, expected_total)
                self.assertEqual(row(n), reference)

    def test_published_small_maximizers(self):
        self.assertEqual(row(3).index(max(row(3))), 2)
        self.assertEqual(row(4).index(max(row(4))), 3)
        self.assertEqual(row(5).index(max(row(5))), 1)

    def test_invalid_range(self):
        for n, m in [(1, 0), (6, 0), (3, -1), (3, 3)]:
            with self.subTest(n=n, m=m):
                with self.assertRaises(ValueError):
                    count_models(n, m)


if __name__ == "__main__":
    unittest.main()
