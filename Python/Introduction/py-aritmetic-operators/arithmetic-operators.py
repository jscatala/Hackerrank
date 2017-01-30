import unittest


def sums(a, b):
    return a + b


def subs(a, b):
    return a - b


def prods(a, b):
    return a * b


class MyTests(unittest.TestCase):
    def testsum(self):
        self.assertEqual(int('5'), sums(3, 2))
        self.assertEqual(int('3'), sums(0, 3))
        self.assertEqual(int('3'), sums(5, -2))

    def testsubs(self):
        self.assertEqual(int(1), subs(3, 2))
        self.assertEqual(int(-1), subs(2, 3))
        self.assertEqual(int(0), subs(3, 3))

    def testprods(self):
        self.assertEqual(int(6), prods(3, 2))
        self.assertEqual(int(0), prods(3, 0))
        self.assertEqual(int(60), prods(3, 20))


if __name__ == '__main__':
    unittest.main()
