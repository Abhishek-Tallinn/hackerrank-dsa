# Problem:  Ema's supercomputer
# Difficulty: Medium
# Link: https://www.hackerrank.com/challenges/two-pluses/problem
# Time Complexity: O(n^6) as we build all the pluses which is O(n^3) and then we do disjoing search in a nested loop which is O(n^2) so square of O(n^3) is O(n^6)
# Space Complexity: O(n^4) as it takes O(n^2) to make a cell set and then O(n^2) further as there are O(n^2) cells so we have to make cell for each center 
# Approach: We iterate over the matrix and for every cell which is G we expand the arms i all direction to see the biggest arm that we can make. 
# Then once arm length is known we run a loop to collect all the cell numbers that will be part of that paricular plus.
# For each plus we append to list a tuple of their area and a set of all the cells. then we come out of main loops and we run a nested loop where we check if each pair of the cells
# is disjoint or not. If they are disjoing and not overlapping we take the maximum area in our ans variable and finally return ans.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoPluses' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY grid as parameter.
#

def twoPluses(grid):
    # Write your code here
    pluses= []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=='G':
                if i==0 or i == len(grid)-1 or j==0 or j==len(grid[0])-1:
                    continue
                left = right = j
                top = down = i
                while left - 1 >= 0 and grid[i][left-1]=='G':
                    left-=1
                while right+1 <len(grid[0]) and grid[i][right+1]=='G': 
                    right+=1
                while top - 1 >= 0 and grid[top-1][j] == 'G':
                    top-=1
                while down + 1< len(grid) and grid[down+1][j]=='G':
                    down+=1
                arm = min(j-left,right-j,i-top,down-i)
                
                
                for arm in range(arm + 1):

                    cells = {(i, j)}

                    for d in range(1, arm + 1):
                        cells.add((i - d, j))
                        cells.add((i + d, j))
                        cells.add((i, j - d))
                        cells.add((i, j + d))

                    area = 4 * arm + 1
                    pluses.append((area, cells))
    ans = 0


    for i in range(len(pluses)):
        area1, cells1 = pluses[i]

        for j in range(i + 1, len(pluses)):
            area2, cells2 = pluses[j]

            if cells1.isdisjoint(cells2):
                ans = max(ans, area1 * area2)
    return ans
                
                    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
