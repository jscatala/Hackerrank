if __name__ == '__main__':
    n = input()
    elements = map(int, input().split())
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    s = sum([(i in a) - (i in b) for i in elements])
    print(s)
