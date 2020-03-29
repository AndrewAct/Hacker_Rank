# 3/24/2020, Tue
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    aBig = 0
    bBig = 0
    for i in range(3):
        if a[i] > b[i]:
            aBig += 1
        elif a[i] < b[i]:
            bBig += 1
        else:
            pass
    return (aBig, bBig)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
