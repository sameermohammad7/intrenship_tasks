#Question5-
#Problem Name - Alternating Characters
#HackerRank Link - https://www.hackerrank.com/challenges/alternating-characters/problem

#You are given a string containing characters A and B only. Your task is to change it into a string such that there are no matching adjacent characters. To do this, you are allowed to delete zero or more characters in the string.
#Your task is to find the minimum number of required deletions.



import math
import os
import random
import re
import sys

# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.

def alternatingCharacters(s):
    # Count how many characters are identical to their preceding character
    deletions = 0
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            deletions += 1
    return deletions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
