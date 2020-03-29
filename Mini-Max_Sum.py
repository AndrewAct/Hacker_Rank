# 3/25/2020, Wed
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    mini = min(arr);
    maxi = max(arr);
    mini_Sum = sum(arr) - max(arr)
    maxi_Sum = sum(arr) - min(arr)
    print(mini_Sum, maxi_Sum)

    

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
