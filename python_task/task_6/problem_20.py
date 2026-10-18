#Question20-
#Problem Name - Validating the Phone Numbe
#HackerRank Link - https://www.hackerrank.com/challenges/validating-the-phone-number/problem


#Let's dive into the interesting topic of regular expressions! You are given some input, and you are required to check whether they are valid mobile numbers.
# A valid mobile number is a ten digit number starting with a 7,8 or 9.

import re

for _ in range(int(input())):
    number = input().strip()
    # Check if the string matches the criteria using a Regular Expression
    # ^[789]: Starts with 7, 8, or 9
    # \d{9}$: Followed by exactly 9 digits, ending the string
    if re.match(r'^[789]\d{9}$', number):
        print("YES")
    else:
        print("NO")

