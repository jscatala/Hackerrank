#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    q = [ k-1 for k in q]
    bribes=0
    for idx, v in enumerate(q):
        if v - idx > 2:
            print("Too chaotic")
            return
        for k in range(max(v-1,0), idx):
            if q[k] > v:
                bribes +=1
    print(bribes)
    
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
