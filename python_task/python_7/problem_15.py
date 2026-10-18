#Question15-
#Problem Name - Game of Thrones - I
#HackerRank Link -https://www.hackerrank.com/challenges/game-of-thrones/problem


#Dothraki are planning an attack to usurp King Robert's throne.
#King Robert learns of this conspiracy from Raven and plans to lock the single door through which the enemy can enter his kingdom.
#But, to lock the door he needs a key that is an anagram of a palindrome.
#He starts to go through his box of strings, checking to see if they can be rearranged into a palindrome.
#Given a string, determine if it can be rearranged into a palindrome. Return the string YES or NO.

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def gameOfThrones(s):
    # Count frequencies of all characters
    freq = Counter(s)
    
    # Count how many characters have an odd frequency
    odd_count = sum(1 for count in freq.values() if count % 2 != 0)
    
    # A palindrome can have at most one odd-frequency character
    return "YES" if odd_count <= 1 else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
