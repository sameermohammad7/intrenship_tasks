#Question1-
#Problem Name - Find the Runner-Up Score!
#HackerRank Link - https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given N scores. Store them in a list and find the score of the runner-up.

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    # Remove duplicate scores using set, then sort them in ascending order
    unique_scores = sorted(set(arr))
    
    # The runner-up is the second highest score (second from the right)
    print(unique_scores[-2])
