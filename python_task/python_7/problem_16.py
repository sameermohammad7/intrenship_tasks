#Question16-
#Problem Name - Caesar Cipher
#HackerRank Link -https://www.hackerrank.com/challenges/caesar-cipher-1/problem


#Julius Caesar protected his confidential information by encrypting it using a cipher.
#Caesar's cipher shifts each letter by a number of letters.
#If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet.
#In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.


import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Normalize the rotation factor to fit within 26 letters
    k = k % 26
    encrypted_chars = []
    
    for char in s:
        if 'a' <= char <= 'z':
            # Rotate lowercase letters
            new_char = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
            encrypted_chars.append(new_char)
        elif 'A' <= char <= 'Z':
            # Rotate uppercase letters
            new_char = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
            encrypted_chars.append(new_char)
        else:
            # Leave symbols, spaces, and digits untouched
            encrypted_chars.append(char)
            
    return "".join(encrypted_chars)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
