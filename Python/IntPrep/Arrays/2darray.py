#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    outputs = list()
    for i in range(4): 
        for j in range(4):
            top = arr[i][j:3+j]
            mid = arr[i+1][j+1]
            bot = arr[i+2][j:3+j]
            outputs.append(sum(top) +mid + sum(bot))
    return max(outputs)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
