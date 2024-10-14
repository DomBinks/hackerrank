#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    counts = [0] * 6
    
    for bird in arr:
        counts[bird] += 1
    
    highestIndex = -1
    highestVal = -1
    for i in range(1, len(counts)):
        if counts[i] > highestVal:
            highestVal = counts[i]
            highestIndex = i
            
    return highestIndex
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

