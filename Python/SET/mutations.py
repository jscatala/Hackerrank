# s.update() or |=
# s.intersection_update() or &=
# s.difference_update() or -=
# s.symmetric_difference_update() or ^=
#


class MySet():
    def __init__(self, set_a):
        self.set_a = set_a
        self.functions = {
            'intersection_update': self.intersection,
            'update': self.update,
            'symmetric_difference_update': self.symmetric,
            'difference_update': self.difference
            }

    def intersection(self, set_b):
        self.set_a &= set_b

    def update(self, set_b):
        self.set_a.update(set_b)

    def symmetric(self, set_b):
        self.set_a ^= set_b

    def difference(self, set_b):
        self.set_a -= set_b

    def sum(self):
        return sum(self.set_a)

    def digest_set(self, operation, set_b):
        self.functions[operation](set_b)


if __name__ == '__main__':
    len_s = int(input())
    myset = MySet(set(map(int, input().split())))
    ops = int(input())
    for i in range(0, ops):
        op = input().split(' ')[0]
        set_b = set(map(int, input().split()))
        myset.digest_set(op, set_b)
    print(myset.sum())
