import unittest
from benchmark import Record, evaluate

class BenchmarkTests(unittest.TestCase):
    def test_known_errors(self):
        r = evaluate([Record("A", -2, -2.5), Record("B", -3, -2), Record("C", -1, -1)])
        self.assertEqual(r["n"], 3)
        self.assertEqual(r["absolute_errors"], [0.5, 1, 0])
        self.assertAlmostEqual(r["mae"], 0.5)
    def test_empty(self):
        with self.assertRaises(ValueError):
            evaluate([])
    def test_duplicate(self):
        with self.assertRaises(ValueError):
            evaluate([Record("A", 0, 1), Record("A", 1, 2)])
    def test_nonfinite(self):
        with self.assertRaises(ValueError):
            evaluate([Record("A", float("nan"), 1)])
    def test_boolean(self):
        with self.assertRaises(ValueError):
            evaluate([Record("A", True, 1)])

if __name__ == "__main__":
    unittest.main()
