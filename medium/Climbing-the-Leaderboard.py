#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    out = [] # Stores the output list
    r = [] # Stores ranked without any duplicates
    prev = -1 # Stores the previous element
    for p in ranked: # For each element in ranked
        if p != prev: # If it's not the same as the previous
            r.append(p) # Add this element to r
        prev = p # Update the previous
        
    # The upper bound of the rank
    lim = len(r)-1 # Start at the last elem in r
    
    for p in player: # For each player
        i = lim # Start at the max possible rank
        
        # While the score is bigger than the score for
        # this rank, and the rank can go lower
        while i > 0 and p > r[i]:
            i-=1 # Decrement the current rank
            
        # Update the upper bound of the rank to this rank
        # as the next score is the same or bigger
        lim = i
        
        # If the score is higher than the highscore
        if(i == 0 and p > r[0]):
            # Must be rank 1
            out.append(1)
        # If the score is the same as the score for this rank
        elif(r[i] == p):
            # Is this rank, +1 as starting from 1 not 0
            out.append(i+1)
        # If the score is lower than the score for this rank
        else:
            # Is the rank below, +2 as starting from 1 not 0
            out.append(i+2)
            
    return out
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

