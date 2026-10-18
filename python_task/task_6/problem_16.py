#Question16-
#Problem Name - Check Subset
#HackerRank Link - https://www.hackerrank.com/challenges/py-check-subset/problem

#The first line will contain the number of test cases, T.
#The first line of each test case contains the number of elements in set A.
#The second line of each test case contains the space separated elements of set A.
#The third line of each test case contains the number of elements in set B.
#The fourth line of each test case contains the space separated elements of set B.

for _ in range(int(input())):
    nA = int(input())
    set_a = set(map(int, input().split()))
    nB = int(input())
    set_b = set(map(int, input().split()))
    
    # Check if set_a is a subset of set_b
    print(set_a.issubset(set_b))
