#Question10-
#Problem Name - Designer Door Mat
#HackerRank Link - https://www.hackerrank.com/challenges/designer-door-mat/problem

#Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
#Mat size must be N X M. (N is an odd natural number, and M is 3 times N .)
#The design should have 'WELCOME' written in the center.
#The design pattern should only use |, . and - characters.

n, m = map(int, input().split())

for i in range(1, n, 2):
    print((".|." * i).center(m, "-"))

print("WELCOME".center(m, "-"))

for i in range(n - 2, 0, -2):
    print((".|." * i).center(m, "-"))
