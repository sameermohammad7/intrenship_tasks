#Question11-
#Problem Name - Designer Door Mat
#HackerRank Link - https://www.hackerrank.com/challenges/designer-door-mat/problem


#Given an integer, n, print the following values for each integer i from 1 to n:
#Decimal
#Octal
#Hexadecimal (capitalized)
#Binary
#Function Description
#Complete the print_formatted function in the editor below.
#print_formatted has the following parameters:
#int number: the maximum value to print



def print_formatted(number):
    width = len(bin(number)) - 2
    for i in range(1, number + 1):
        print(f"{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
