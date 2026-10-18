#Question5-
#Problem Name - Write a Function
#HackerRank Link - https://www.hackerrank.com/challenges/write-a-function/problem

#Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

def is_leap(year):
    leap = False
    
    # A leap year is evenly divisible by 4, 
    # except when it is evenly divisible by 100, 
    # unless it is also evenly divisible by 400.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap = True
        
    return leap

year = int(input())
print(is_leap(year))

