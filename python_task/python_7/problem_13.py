#Question13-
#Problem Name - Sherlock and the Valid String
#HackerRank Link - https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem


#Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just 1 character at 1 index in the string, and the remaining characters will occur the same number of times. Given a string s, determine if it is valid.
#If so, return YES, otherwise return NO.


#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Step 1: Count frequency of each character
    char_counts = Counter(s)
    
    # Step 2: Count frequency of the frequencies
    freq_counts = Counter(char_counts.values())
    
    # All characters already have the exact same frequency
    if len(freq_counts) == 1:
        return "YES"
    
    # More than two distinct frequencies cannot be fixed with 1 removal
    if len(freq_counts) > 2:
        return "NO"
    
    # Exactly two frequencies exist: sort by frequency value
    # (f1, c1) is the lower frequency, (f2, c2) is the higher frequency
    (f1, c1), (f2, c2) = sorted(freq_counts.items())
    
    # Subcase A: The lowest frequency is 1 and occurs on exactly one character (e.g., 'aabbc')
    # Removing this single character leaves all remaining characters with frequency f2
    if f1 == 1 and c1 == 1:
        return "YES"
        
    # Subcase B: The higher frequency is exactly 1 higher than the lower frequency,
    # and occurs on only 1 character (e.g., 'aabbccc' -> f1=2, f2=3, c2=1)
    if f2 - f1 == 1 and c2 == 1:
        return "YES"
        
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
