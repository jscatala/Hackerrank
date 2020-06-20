#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    socks_d = dict()
    pairs = 0
    for sock in ar:
        if not sock in socks_d:
            socks_d[sock] = 1
        else:
            socks_d[sock] += 1
            if (socks_d[sock] % 2 ) == 0 :
                socks_d[sock] = 0
                pairs = pairs + 1 
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
