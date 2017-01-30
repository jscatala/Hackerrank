import unittest


def in_range(x):
    if x in range(6, 21):
        return True
    return False


def is_odd(x):
    if x % 2 == 0:
        return False
    return True


def is_weird(x):
    flag = 'Not Weird'
    if is_odd(x) or in_range(x):
        flag = 'Weird'
    return flag


class MyTests(unittest.TestCase):
    def test(self):
        self.assertEqual('Weird', is_weird(3))
        self.assertEqual('Not Weird', is_weird(24))


if __name__ == '__main__':
    unittest.main()
