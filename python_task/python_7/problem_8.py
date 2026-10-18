#Question8-
#Problem Name - Gemstones
#HackerRank Link - https://www.hackerrank.com/challenges/gem-stones/problem

#There is a collection of rocks where each rock has various minerals embeded in it. Each type of mineral is designated by a lowercase letter in the range ascii[a - z].
#There may be multiple occurrences of a mineral in a rock. A mineral is called a gemstone if it occurs at least once in each of the rocks in the collection.
#Given a list of minerals embedded in each of the rocks, display the number of types of gemstones in the collection.

import math
import os
import random
import re
import sys

#
# Complete the 'gemstones' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY arr as parameter.
#

def gemstones(arr):
    # Find the set of characters common to all strings
    common_minerals = set(arr[0])
    for rock in arr[1:]:
        common_minerals &= set(rock)
        
    return len(common_minerals)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
