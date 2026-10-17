#Question5-
#Problem Name - String Validators
#HackerRank Link - https://www.hackerrank.com/challenges/string-validators/problem

#Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.

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

