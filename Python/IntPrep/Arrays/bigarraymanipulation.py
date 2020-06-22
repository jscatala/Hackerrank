#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0]*(n+1)
    for query in queries:
        head, tail, number = query
        arr[head] += number
        if (tail+1) <= n:
            arr[tail+1] -=number
    x = ma = 0
    for i in arr:
        x += i
        if (ma < x ):
            ma = x
    return ma

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
