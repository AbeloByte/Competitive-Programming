#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    no = arr[-1]
    k = n - 2
    while k >= 0 and arr[k] > no:
        arr[k + 1] = arr[k]
        print(*arr)
        k -= 1
    arr[k + 1] = no
    print(*arr)
            
            
            
            

if __name__ == '__main__':
    
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)
    













