#Question6-
#Problem Name - Pangrams
#HackerRank Link - https://www.hackerrank.com/challenges/pangrams/problem


#A pangram is a string that contains every letter of the alphabet.
#Given a sentence determine whether it is a pangram in the English alphabet.
#Ignore case. Return either pangram or not pangram as appropriate.


import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Extract unique letters from the string (ignoring case and non-alphabetic characters)
    alphabet_set = set(char for char in s.lower() if char.isalpha())
    
    # Check if we have all 26 letters
    if len(alphabet_set) == 26:
        return "pangram"
    else:
        return "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
