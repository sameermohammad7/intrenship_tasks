#Question3-
#Problem Name - Mars Exploration
#HackerRank Link - https://www.hackerrank.com/challenges/validating-the-phone-number/problem?utm_source=chatgpt.com



#A space explorer's ship crashed on Mars! They send a series of SOS messages to Earth for help.
#Letters in some of the SOS messages are altered by cosmic radiation during transmission. Given the signal received by Earth as a string, , determine how many letters of the SOS message have been changed by radiation.


#!/bin/python3

import math
import os
import random
import re
import sys

def marsExploration(s):
    # Count how many characters differ from the expected 'SOS' pattern
    count = 0
    expected = "SOS"
    
    for i in range(len(s)):
        # Check if the current character matches the corresponding position in 'SOS'
        if s[i] != expected[i % 3]:
            count += 1
            
    return count

if __name__ == '__main__':
    fout = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fout.write(str(result) + '\n')

    fout.close()
