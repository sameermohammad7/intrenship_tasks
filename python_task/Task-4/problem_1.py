#question1 - The provided code stub reads two integers from STDIN,  and . Add code to print three lines where: 
 #The first line contains the sum of the two numbers 
 #The second line contains the difference of the two numbers (first - second) 
  #The third line contains the product of the two numbers.

#code-
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    
    if n % 2 != 0:
        print("Weird")
    
    else:
        if n >= 2 and n <= 5:
            print("Not Weird")
        elif n >= 6 and n <= 20:
            print("Weird")
        elif n > 20:
            print("Not Weird")
