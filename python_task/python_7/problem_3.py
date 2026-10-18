#Question3-
#Problem Name - Mars Exploration
#HackerRank Link - https://www.hackerrank.com/challenges/validating-the-phone-number/problem?utm_source=chatgpt.com



#A space explorer's ship crashed on Mars! They send a series of SOS messages to Earth for help.
#Letters in some of the SOS messages are altered by cosmic radiation during transmission. Given the signal received by Earth as a string, , determine how many letters of the SOS message have been changed by radiation.


import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    count = 0
    expected = "SOS"
    
    for i in range(len(s)):
        # Compare each character with the expected 'SOS' pattern
        if s[i] != expected[i % 3]:
            count += 1
            
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
