#Question11-
#Problem Name - String Validators
#HackerRank Link - https://www.hackerrank.com/challenges/string-validators/problem

#You are given a string .
# Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.  
#  Input Format
#   A single line containing a string S.

if __name__ == '__main__':
    s = input()
    
    # 1. Check for any alphanumeric characters
    print(any(c.isalnum() for c in s))
    
    # 2. Check for any alphabetical characters
    print(any(c.isalpha() for c in s))
    
    # 3. Check for any digits
    print(any(c.isdigit() for c in s))
    
    # 4. Check for any lowercase characters
    print(any(c.islower() for c in s))
    
    # 5. Check for any uppercase characters
    print(any(c.isupper() for c in s))
