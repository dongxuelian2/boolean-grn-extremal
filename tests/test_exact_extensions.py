"""Extended exact rows, with independent slice and alternative-pivot checks."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from count_full_multistability import count_models, row
from slice_counts import monotone_tables, slice_row

ROWS = {
    6: [6894, 303616, 486136, 89536, 7413, 15160],
    7: [7785062, 15441839115, 145806103409, 45459722472,
        875055125, 7820773, 15656706],
}


class ExactExtensions(unittest.TestCase):
    def test_independent_slices(self):
        self.assertEqual([len(monotone_tables(d)) for d in range(6)],
                         [2, 3, 6, 20, 168, 7581])
        for n in range(2, 7):
            self.assertEqual(slice_row(n), row(n))

    def test_extended_rows_both_pivots(self):
        for n, expected in ROWS.items():
            for pivot in ('lowest', 'highest'):
                self.assertEqual([count_models(n, m, pivot=pivot) for m in range(n)], expected)
            self.assertEqual([m for m, v in enumerate(expected) if v == max(expected)], [2])

    def test_one_activator_identity(self):
        d = [2, 3, 6, 20, 168, 7581, 7828354]
        for n in range(2, 8):
            self.assertEqual(count_models(n, n-2), d[n-1]-d[n-2])
            self.assertLess(count_models(n, n-2), count_models(n, n-1))

    def test_invalid_parameters(self):
        with self.assertRaises(ValueError):
            count_models(3, 1, pivot='unknown')
        with self.assertRaises(ValueError):
            slice_row(7)
        with self.assertRaises(ValueError):
            monotone_tables(6)

class WeightedIntervals(unittest.TestCase):
    def test_three_boundary_slices(self):
        from slice_counts import two_activator_counts
        for m in range(5):
            values = two_activator_counts(m)
            self.assertEqual(values, tuple(count_models(m+3, k) for k in (m, m+1, m+2)))
            if m >= 2:
                self.assertGreater(values[0], values[2])
                self.assertGreaterEqual(values[0]-values[2], 145*m*(m-1)//2-13*m-8)
                self.assertGreater(values[2], values[1])
