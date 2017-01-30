if __name__ == '__main__':
    n = input()
    a = set(map(int, input().split()))
    n = input()
    b = set(map(int, input().split()))
    u = a.union(b)
    i = a.intersection(b)
    d_list = list(u.difference(i))
    d_list.sort()
    for x in d_list:
        print(x)
