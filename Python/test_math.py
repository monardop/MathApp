import unittest
import fractions


class MyTestCase(unittest.TestCase):
    def test_string(self):
        a = fractions.Fraction(32, 9)
        self.assertEqual(str(a), "32/9")

    def test_sqrt(self):
        a = fractions.Fraction(25, 9)
        self.assertEqual(a**(1/2), 5/3)

    def test_decimal(self):
        a = fractions.Fraction(30, 6)
        b = a.get_decimal()
        self.assertEqual(b, 5)

    def test_division(self):
        a = fractions.Fraction(10, 6)
        b = fractions.Fraction(6, 10)
        self.assertEqual(str(a/b), "25/9")

    def test_mixed(self):
        a = fractions.Fraction(25, 9)
        self.assertEqual(a.get_mix_fraction(), "2 7/9")


if __name__ == '__main__':
    unittest.main()
