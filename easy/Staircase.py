#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    current = 1
    while current <= n:
        spaces = " " * (n-current)
        hashes = "#" * current
        out = spaces + hashes
        print(out)
        current += 1

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)

