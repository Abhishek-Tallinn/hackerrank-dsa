# Problem:  The grid search
# Difficulty: Medium
# Link: https://www.hackerrank.com/challenges/the-grid-search
# Time Complexity: O(R*C*r*c) where R, C are dimensions of the grid and r, c are dimensions of the pattern
# Space Complexity: O(c) as we only store the slice
# Approach: We iterate through each row in the grid and check if the pattern matches at that position.
# If there is a match we start a while loop as matching can start at multiple places. For every start we match the string by clicing in the next rows which is equal to the depth of the pattern
# If all checks succeed then we return YES. If for loop end without returning then we know it cannot be found so we return NO


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#

def gridSearch(G, P):
    # Write your code here
    depth = len(P)
    width = len(P[0])
    for i in range(len(G)-depth+1):
        start = G[i].find(P[0])
        while start !=-1:
            
            isPossible = True
            # do everything in this block
            #for j in range(1,len(P)):
            if all(G[i+j][start:start+width] == P[j] for j in range(1,len(P))):
                return "YES"
                    #isPossible = False
                    #break
            #if isPossible:
            #    return "YES"
            start = G[i].find(P[0],start+1)
            
    return "NO"
    
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
