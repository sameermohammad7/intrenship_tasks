#Problem Name - Loops
#HackerRank Link - https://www.hackerrank.com/challenges/python-loops/problem


#Task
The provided code stub reads an integer, , from STDIN. For all non-negative integers i < n , print i² .

Example
n = 3

The list of non-negative integers that are less than n = 3 is [1,2,3]. Print the square of each number on a separate line.

if __name__ == '__main__':
    n = int(input())
    
    for i in range(n):
        print(i ** 2)
