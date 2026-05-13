# Problem: Bigger is greater
# Difficulty: Medium
# Link: https://www.hackerrank.com/challenges/bigger-is-greater/problem?isFullScreen=true
# Time Complexity: O(n) as we do two passes on array
# Space Complexity: O(n) as we use an a list converted from string and we do a reversal at end.
# Approach: The question is about finding the "next greater permutation or 'dicionary order'
# We iterate from right to left and find the first element which is decreasing as we have to make the switch at this point
# then this element is switches with its immediately higher character somewhere on its right side.
# this will make the string on the right of this character in descending order. Hence we reverse the remaining string w[i+1:] and this gives us the next higher lexicographical string.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    # Write your code here
    w = [char for char in w]
    i = len(w)-2
    while i >=0 and w[i]>=w[i+1]:
        i-=1
    
    if i == -1:
        return "no answer"
    j = len(w)-1
    while w[j]<=w[i]:
        j-=1
    # then we swap with next greater elements
    w[i],w[j] = w[j],w[i]
    
    #reverse the rest of it
    w[i+1:] = w[i+1:][::-1]
    return ''.join(w)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
