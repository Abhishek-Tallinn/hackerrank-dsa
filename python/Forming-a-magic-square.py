# Problem: Forming a magic square
# Difficulty: Easy
# Link: https://www.hackerrank.com/challenges/magic-square-forming/problem
# Time Complexity: O(n^2) as we do passes on a 2D array
# Space Complexity: O(k) as we use a matrix list to match with
# Approach: The question needs the realization that theer are only 8 possible magic squares and then cost of acheiving each can be brute forced and calculated.
# Deriving a general algorithm to find the cost of acheiving a magic square is not possible as there is state explosion.
# 
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    # Write your code here
    magic_squares = [
    [
        [8, 1, 6],
        [3, 5, 7],
        [4, 9, 2]
    ],
    [
        [6, 1, 8],
        [7, 5, 3],
        [2, 9, 4]
    ],
    [
        [4, 9, 2],
        [3, 5, 7],
        [8, 1, 6]
    ],
    [
        [2, 9, 4],
        [7, 5, 3],
        [6, 1, 8]
    ],
    [
        [8, 3, 4],
        [1, 5, 9],
        [6, 7, 2]
    ],
    [
        [4, 3, 8],
        [9, 5, 1],
        [2, 7, 6]
    ],
    [
        [6, 7, 2],
        [1, 5, 9],
        [8, 3, 4]
    ],
    [
        [2, 7, 6],
        [9, 5, 1],
        [4, 3, 8]
    ]
]
    min_cost = float('inf')
    def calculate(a,b):
        total = 0
        for i in range(3):
            for j in range(3):
                total+=abs(a[i][j]-b[i][j])
        return total
    for sq in magic_squares:
        cost = calculate(s,sq)
        min_cost = min(min_cost,cost)
    return min_cost
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
