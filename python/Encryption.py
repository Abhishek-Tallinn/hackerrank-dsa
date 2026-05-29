# Problem:  Encryption
# Difficulty: Medium
# Link: https://www.hackerrank.com/challenges/encryption/
# Time Complexity: O(rows * cols) as we do pass on the 2D array.
# Space Complexity: O(rows * cols) as we use a 2D array to store the characters.
# Approach: We first remove spaces and calculate the dimensions of the 2D array.
# Then we fill the array row-wise and transpose it to get the encrypted string and we return after stripping any trailing whitespaces.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    if len(s)==1:
        return s
    # Write your code here
    l = ''.join([char for char in s if char!=' '])
    L = len(l)
    rows = math.isqrt(L) 
    cols = math.ceil(math.sqrt(L))
    while rows*cols<L:
        rows+=1
    k = 0
    dp = [['' for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            dp[i][j] = l[k]
            if k == L-1:
                break
            k+=1
        
    col_matrix = [list(row) for row in zip(*dp)]
    ans = []
    for row in col_matrix:
        ans.extend(row)
        ans.append(' ')
    return ''.join(ans).rstrip()
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
