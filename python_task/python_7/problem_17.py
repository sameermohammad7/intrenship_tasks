#Question17-
#Problem Name - Separate the Numbers
#HackerRank Link -https://www.hackerrank.com/challenges/separate-the-numbers/problem


#$a_{i} - a_{i-1} = 1$ for all $1 < i \le k$ (strictly increasing by $1$).
#No number contains a leading zero
#(e.g., "01" is invalid).The original string is formed by concatenating these numbers directly.


import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    n = len(s)
    
    # Strings of length 1 or strings starting with '0' cannot be beautiful
    if n <= 1 or s[0] == '0':
        print("NO")
        return

    # Try every possible length for the first number (up to half the string's length)
    for length in range(1, n // 2 + 1):
        first_num = int(s[:length])
        current_num = first_num
        built_string = str(current_num)
        
        # Build the sequence by incrementing current_num by 1
        while len(built_string) < n:
            current_num += 1
            built_string += str(current_num)
            
        # If the constructed string matches the target string exactly
        if built_string == s:
            print(f"YES {first_num}")
            return
            
    print("NO")


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input().strip()

        separateNumbers(s)


