import unittest


def get_squares(n):
    return map(lambda x: x**2, range(0, n))


def print_squares(x):
    for i in get_squares(x):
        print(i)


class MyTests(unittest.TestCase):
    def testsquares(self):
        self.assertEqual([0, 1, 4, 9], get_squares(4))
        self.assertEqual([0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144],
                         get_squares(13))


if __name__ == '__main__':
    unittest.main()
