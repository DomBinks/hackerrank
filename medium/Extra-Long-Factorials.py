#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    #print(str(math.factorial(n)))
    
    c = n
    
    for i in range(1,n):
        c *= i
        
    print(str(c))

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)

