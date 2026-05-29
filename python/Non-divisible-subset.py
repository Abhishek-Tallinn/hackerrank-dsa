# Problem:  Non-divisible subset
# Difficulty: Medium
# Link: https://www.hackerrank.com/challenges/non-divisible-subset/
# Time Complexity: O(n) as we do a single pass through the numbers from 1 to n.
# Space Complexity: O(n) as we only use a dictionary to hold remainders
# Approach: We make a dictionary with remainders because if a number with remainder r has been chosen in our maximal subset a number with k-r cannot be chosen. But we also need to keep in mind that 
# since we need maximal subset it two number with remainders r and k-r clash we chose the one which has more frequencey. Therefore we make a freq hashmap of remainders. 
# At start of loop we set to count to min of freq[0] and 1 as if there is a number with remainder 0 we only want one of those so we take minimum. 
# then we loop till k//2 as we dont want to count duplicate pairs. In loop if we find r is equal to k-r meaning the remainder is exactly in the middle then we can only take one such number
# and the frequency would not matter. So we increment count by 1 in this case also. Then we return count.

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    freq = Counter(x%k for x in s)
    count = min(freq[0],1)
    for r in range(1,(k//2)+1):
        
        if r == k-r:
            count+=1
        else:
            count+= max(freq[r],freq[k-r])
    return count   
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
