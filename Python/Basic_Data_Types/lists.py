# List Commands:
# insert(index, obj)
# print
# remove(obj)
# append(obj)
# sort
# pop
# reverse
#


class MyList(object):
    def __init__(self):
        self.__my_list = list()
        self.___functions = {
            'insert': self._insert,
            'print': self._print,
            'remove': self._remove,
            'append': self._append,
            'sort': self._sort,
            'pop': self._pop,
            'reverse': self._reverse
        }

    def _insert(self, idx, e):
        self.my_list.insert(idx, e)

    def _print(self):
        print(self.my_list)

    def _remove(self, e):
        self.my_list.remove(e)

    def _append(self, e):
        self.my_list.append(e)

    def _sort(self):
        self.my_list.sort()

    def _pop(self):
        self.my_list.pop()

    def _reverse(self):
        self.my_list.reverse()

    def digest_line(self, args):
        line = args.split()
        if len(line) == 2:
            self._functions[line[0]](int(line[1]))
        elif len(line) == 3:
            self._functions[line[0]](int(line[1]), int(line[2]))
        else:
            self._functions[line[0]]()


if __name__ == '__main__':
    N = int(input())
    my_list = MyList()
    for i in range(0, N):
        my_list.__digest_line(input())
