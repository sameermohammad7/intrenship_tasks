#Question10-
#Problem Name - CamelCase
#HackerRank Link - https://www.hackerrank.com/challenges/camelcase/problem


#There is a sequence of words in CamelCase as a string of letters, s,having the following properties:
#It is a concatenation of one or more words consisting of English letters.
#All letters in the first word are lowercase.
#For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.

import math
import os
import random
import re
import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def camelcase(s):
    # The first word starts lowercase, and each subsequent word starts with an uppercase letter
    return 1 + sum(1 for char in s if char.isupper())


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()

