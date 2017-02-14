#Palindrome Problem
from itertools import permutations


def get_strings(s):
    mid = int(len(s)/2)
    left = s[:mid]
    if len(s)%2 == 0:
        right = s[mid:]
    else:
        right = s[mid+1:]
    return left, right

def is_plindrome(s):
    # s is a string -> 'aabbbb'
    # returns a 'YES'
    flag = 'NO'
    for i in permutations(s):
        l,r = get_strings(i)
        if l == r :
            flag = 'YES'
            break
    print(flag)

######################## 
# Compress problem 

from itertools import groupby

def get_count(s):
    # s is an string -> 'aaaabbbaaxcdeeddssfeeeddd'
    # l is a list -> ['a', 6, 'b', 3, 'c', 1, 'd', 6, 'e', 5, 'f', 1, 's', 2, 'x', 1]
    l=list()
    s_l=list(s)
    s_l.sort()
    [l.extend((k, len(list(group)))) for k, group in groupby(s_l)]
    return l
