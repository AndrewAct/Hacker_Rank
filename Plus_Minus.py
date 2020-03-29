# 3/23/2020, Mon 
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.

def plusMinus(arr):
    pos, neg, z = 0, 0, 0
    for i in range(len(arr)):
        if arr[i] > 0:
            pos += 1
        elif arr[i] < 0:
            neg += 1
        else:
            z += 1
    print(pos/len(arr))
    print(neg/len(arr))
    print(z/len(arr))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
