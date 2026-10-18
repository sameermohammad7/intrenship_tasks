#Question14-
#Problem Name - Set .intersection() Operation
#HackerRank Link - https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

#The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed only to French, and some have subscribed to both newspapers.
#You are given two sets of student roll numbers. One set has subscribed to the English newspaper, one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to both newspapers.

n = int(input())
set_english = set(map(int, input().split()))
b = int(input())
set_french = set(map(int, input().split()))

# Find the intersection of both sets and print the length
print(len(set_english.intersection(set_french)))
