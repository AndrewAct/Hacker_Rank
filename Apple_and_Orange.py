# 4/3/2020, Fri
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple = 0
    orange = 0
    for i in range(len(apples)):
        distance1 = a + apples[i]
        if distance1 in range(s, t+1):
            apple += 1
    for i in range(len(oranges)):
        distance2 = b + oranges[i]
        if distance2 in range(s, t+1):
            orange += 1
    print(apple)
    print(orange)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
