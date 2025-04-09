#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    checker = n % 2
    if checker == 0 and 2 <= n <= 5 : 
        print("Not Weird")
    elif checker == 0 and 20 < n: 
        print("Not Weird")
    else:
        print("Weird")
