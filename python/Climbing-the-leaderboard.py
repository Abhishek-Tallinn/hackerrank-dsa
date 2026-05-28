# Problem:  Climbing the leaderboard
# Difficulty: Medium
# Link: https://www.hackerrank.com/challenges/climbing-the-leaderboard/
# Time Complexity: O(n log n) as we do pass on ranked array and then on player array with a nested binary search.
# Space Complexity: O(n) as we use a pre computed rank list
# Approach: Since ranks are repetitive we first compute the rank list and then for each player score we do a binary search on ranked array to find the position where it can be inserted 
# and then we return the rank at that position. We also handle edge cases where player score is less than lowest score or greater than highest score.
# Since ranked array has repeated values we handle that in binary search as well

#!/bin/python3

import math
import os
import random
import re
import sys
import bisect
#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    res = [0]*len(player)
    pre_ranks = [1]
    for i in range(1,len(ranked)):
        if ranked[i] == ranked[i-1]:
            pre_ranks.append(pre_ranks[-1])
        else:
            pre_ranks.append(pre_ranks[-1]+1)
    # now we have rank pos now find insertion pos
    for i in range(len(player)):
        if player[i] < ranked[-1]:
            res[i] = pre_ranks[-1]+1
            continue
        if player[i] > ranked[0]:
            res[i] = pre_ranks[0] 
            continue
        #else we calculate position
        left, right = 0 , len(ranked)-1
        while left<right:
            mid = (left+right)//2
            if ranked[mid] > player[i]:
                left = mid+1
            elif ranked[mid] <= player[i]:
                right = mid
            else:
                right = right-1
        res[i] = pre_ranks[left] 
    return res  
    
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