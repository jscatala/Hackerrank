import unittest


def div_integer(x, y):
    return x // y


def div_float(x, y):
    return float(x) / y


class MyTests(unittest.TestCase):
    def testinteger(self):
        self.assertEqual(int(1), div_integer(4, 3))
        self.assertEqual(int(0), div_integer(6, 7))
        self.assertEqual(int(4), div_integer(12, 3))

    def testfloat(self):
        self.assertEqual(1.3333333333333333, div_float(4, 3))
        self.assertEqual(0.8571428571428571, div_float(6, 7))
        self.assertEqual(4.0, div_float(12, 3))


if __name__ == '__main__':
    unittest.main()
