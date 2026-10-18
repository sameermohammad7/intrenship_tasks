#Question14-
#Problem Name - Anagram
#HackerRank Link - https://www.hackerrank.com/challenges/anagram/problem

#Two words are anagrams of one another if their letters can be rearranged to form the other word.
#Given a string, split it into two contiguous substrings of equal length. Determine the minimum number of characters to change to make the two substrings into anagrams of one another.

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    n = len(s)
    
    # If the length is odd, it cannot be split into two equal halves
    if n % 2 != 0:
        return -1
    
    mid = n // 2
    s1 = s[:mid]
    s2 = s[mid:]
    
    c1 = Counter(s1)
    c2 = Counter(s2)
    
    # (c1 - c2) keeps only the positive differences (characters needing to be replaced)
    return sum((c1 - c2).values())


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
