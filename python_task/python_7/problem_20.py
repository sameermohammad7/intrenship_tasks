#Question20-
#Problem Name - Super Reduced String
#HackerRank Link -https://www.hackerrank.com/challenges/weighted-uniform-string/problem

#Reduce a string of lowercase characters in range ascii[‘a’..’z’]by doing a series of operations.
#In each operation, select a pair of adjacent letters that match, and delete them.
#Delete as many characters as possible using this method and return the resulting string. If the final string is empty, return Empty String


import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    stack = []
    
    for char in s:
        # If the current character matches the previous, eliminate the pair
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
            
    # Return the joined string or "Empty String" if completely reduced
    return "".join(stack) if stack else "Empty String"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
