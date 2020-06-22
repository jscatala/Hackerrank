#!/bin/python3

import math
import os
import random
import re
import sys

def get_dict(l):
    d = dict()
    for word in l:
        if word in d:
            d[word] += 1
        else:
            d[word] =1
    return d

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    note_d = get_dict(note)
    mag_d = get_dict(magazine)

    can = "Yes"
    for word in note_d.keys():
        if word not in mag_d.keys() or mag_d[word] < note_d[word]:
                can = "No"
                pass

    print(can)
    

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
