#Question4-
#Problem Name - Funny String
#HackerRank Link - https://www.hackerrank.com/challenges/validating-the-phone-number/problem?utm_source=chatgpt.com

#In this challenge, you will determine whether a string is funny or not. To determine whether a string is funny, create a copy of the string in reverse e.g. abc-->cba. Iterating through each string, compare the absolute difference in the ascii values of the characters at positions 0 and 1, 1 and 2 and so on to the end. If the list of absolute differences is the same for both strings, they are funny.
#Determine whether a give string is funny. If it is, return Funny, otherwise return Not Funny.

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    # Create the reverse of the string
    r = s[::-1]
    
    # Calculate absolute differences of adjacent character ASCII values for both strings
    s_diffs = [abs(ord(s[i]) - ord(s[i+1])) for i in range(len(s) - 1)]
    r_diffs = [abs(ord(r[i]) - ord(r[i+1])) for i in range(len(r) - 1)]
    
    # Compare the difference lists
    if s_diffs == r_diffs:
        return "Funny"
    else:
        return "Not Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
