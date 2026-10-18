#Question18-
#Problem Name - String Construction
#HackerRank Link -https://www.hackerrank.com/challenges/string-construction/problem


#Amanda has a string of lowercase letters that she wants to copy to a new string. She can perform the following operations with the given costs.
#She can perform them any number of times to construct a new string p:
#Append a character to the end of string p at a cost of 1 dollar.
#Choose any substring of p and append it to the end of p at no charge.

import math
import os
import random
import re
import sys

#
# Complete the 'stringConstruction' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def stringConstruction(s):
    # Cost is equal to the number of distinct characters in the string
    return len(set(s))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = stringConstruction(s)

        fptr.write(str(result) + '\n')

    fptr.close()

  
