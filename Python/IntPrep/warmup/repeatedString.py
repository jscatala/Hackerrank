#!/bin/python3

import math
import os
import random
import re
import sys

def get_count(s):
    return len([ 1 for i in s if i == 'a'])
# Complete the repeatedString function below.
def repeatedString(s, n):
    aes = 0
    if len(s)<n:
        aes = get_count(s)
    mod = n%len(s)
    mod_aes = 0
    if mod != 0:
        mod_aes = get_count(s[:mod])
    return aes*(n//len(s)) + mod_aes
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
