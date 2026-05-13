# Problem: 2D array
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/2d-array/submissions/code/472078383
# Time Complexity: O(n^2) as we do one pass on a 2D array
# Space Complexity: O(1) as we dont make a new data structure and the slices we do are on fixed length 3
# Approach: THe approach is straighforward to iterate through the matrix and slice the required elements and add them and we keep a max_sum which we keep updating in every iteration.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    max_sum = float('-inf')
    for i in range(len(arr)-2):
        for j in range(len(arr[0])-2):
            temp_sum = sum(arr[i][j:j+3])
            temp_sum += arr[i+1][j+1]
            temp_sum += sum(arr[i+2][j:j+3])
            max_sum = max(max_sum,temp_sum)
            temp_sum=0
    return max_sum
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
