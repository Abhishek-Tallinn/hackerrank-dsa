# Problem:  Larry's Array
# Difficulty: Medium
# Link: https://www.hackerrank.com/challenges/larrys-array/
# Time Complexity: O(n^2) as we run nested loops and count inversions
# Space Complexity: O(1) as we only have two pointers i and j
# Approach: The solution may look simple but this question is about observation. We need to observe that Larry's move is an even permutation and hence it preserves the permutation parity of the original permutation given in the test case.
# and our target is sorted array which has 0 inversions and hence has even parity. So to reach a permutation of even parity, since our moves preserves the parity
# we must start from a permutation of even parity to reach sorted state. If we start from odd, then we can never change the permutaion parity and cannot arrive at sorted array.
# Once we have this observation in place, we just count the total number of inversions in given array and if its even then it means we can reach sorted state and we return YES or else NO.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'larrysArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY A as parameter.
#

def larrysArray(A):
    # Write your code here
    inv = 0
    for i in range(n):
        for j in range(i+1,n):
            if A[i] > A[j]:
                inv+=1
    return "YES" if inv%2==0 else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
