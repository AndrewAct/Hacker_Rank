# 4/4/2020, Sat 
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    maxi = scores[0] 
    mini = scores[0]
    maCount = 0
    miCount = 0
    for i in range(len(scores)):
        if scores[i]> maxi:
            maxi = scores[i]
            maCount += 1
        if scores[i]<mini:
            mini = scores[i]
            miCount += 1
    return maCount, miCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
