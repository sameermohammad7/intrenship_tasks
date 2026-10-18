#Question11-
#Problem Name - Two Strings
#HackerRank Link - https://www.hackerrank.com/challenges/two-strings/problem

#Given two strings, determine if they share a common substring. A substring may be as small as one character.


import math
import os
import random
import re
import sys

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def twoStrings(s1, s2):
    # If the set intersection is non-empty, they share at least one character (common substring)
    return "YES" if set(s1) & set(s2) else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()

