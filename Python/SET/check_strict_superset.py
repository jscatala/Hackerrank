if __name__ == '__main__':
    A = set(map(int, input().split()))
    n = int(input())
    flag = True
    while n:
        n = n-1
        B = set(map(int, input().split()))
        if not A.issuperset(B):
            flag = False
            n = 0
    print(flag)
