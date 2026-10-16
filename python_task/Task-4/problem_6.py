#Question6-
#Problem Name - Find the Runner-Up Score!
#HackerRank Link - https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.
# Input Format
#  The first line contains n. The second line contains an array A[]  of n integers each separated by a space.

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    # Remove duplicate scores using set, then sort them in ascending order
    unique_scores = sorted(set(arr))
    
    # The runner-up is the second highest score (second from the right)
    print(unique_scores[-2])
