#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hourString = ""
    if s[8:] == "PM" and s[0:2] != "12":
        hour = int(s[0:2])
        hour += 12
        hourString = str(hour)
    
    if s[8:] == "AM" and s[0:2] == "12":
        hourString = "00"
        
    if hourString != "":
        newS = hourString
        newS += s[2:]
        s = newS
        
    return s[:-2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close(
