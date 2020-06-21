#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    arr = [ n-1 for n in arr ]
    arr_w_index=[*enumerate(arr)]
    visited = { k:False for k in range(len(arr)) }
    i = 0
    swaps = 0
    while i < len(arr):
        lines = 0
        while not visited[i]:
            visited[i] = True
            if arr_w_index[i][1] != i:
                lines += 1
                i = arr_w_index[i][1]
        i += 1
        if lines != 0:
            swaps += lines - 1
    return swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
