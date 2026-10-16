#Question13-
#Problem Name - Symmetric Difference
#HackerRank Link - https://www.hackerrank.com/challenges/symmetric-difference/problem

#Task
# Given  sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both.
#  Input Format
#   The first line of input contains an integer, M.
#    The second line contains M space-separated integers.
#      The third line contains an integer, N.
#        The fourth line contains N space-separated integers.


if __name__ == '__main__':
    # Read the size and elements of the first set
    m = int(input())
    a = set(map(int, input().split()))
    
    # Read the size and elements of the second set
    n = int(input())
    b = set(map(int, input().split()))
    
    # Find symmetric difference and sort in ascending order
    diff = sorted(a.symmetric_difference(b))
    
    # Print each value on a new line
    for val in diff:
        print(val)
