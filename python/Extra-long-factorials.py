# Problem:  Extra long factorials
# Difficulty: Medium
# Link: https://www.hackerrank.com/challenges/extra-long-factorials/
# Time Complexity: O(n) as we do a single pass through the numbers from 1 to n.
# Space Complexity: O(1) as we only use a constant amount of extra space.
# Approach: We calculate the factorial via recursion and handle large numbers by using Python's built-in support for arbitrary precision integers.


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
    # Write your code here
    def factorial(n):
        if n== 1:
            return 1
        return n*factorial(n-1)
    
    print(factorial(n))
    

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
