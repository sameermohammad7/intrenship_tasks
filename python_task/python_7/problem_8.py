#Question9-
#Problem Name - Beautiful Binary String
#HackerRank Link - https://www.hackerrank.com/challenges/beautiful-binary-string/problem

#Alice has a binary string. She thinks a binary string is beautiful if and only if it doesn't contain the substring "010".
#In one step, Alice can change a to a or vice versa. Count and print the minimum number of steps needed to make Alice see the string as beautiful.

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulBinaryString' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING b as parameter.
#

def beautifulBinaryString(b):
    # Each non-overlapping "010" requires exactly 1 change
    return b.count('010')


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()

