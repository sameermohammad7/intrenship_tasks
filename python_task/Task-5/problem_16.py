#Question16-
#Problem Name - Collections.Counter()
#HackerRank Link - https://www.hackerrank.com/challenges/collections-counter/problem

#Task
# Raghu is a shoe shop owner. His shop has X number of shoes.
#  He has a list containing the size of each shoe he has in his shop.
#   There are N number of customers who are willing to pay Xi amount of money only if they get the shoe of their desired size.
#    Your task is to compute how much money Raghu earned.

from collections import Counter

if __name__ == '__main__':
    # Number of shoes in the shop
    x = int(input())
    
    # Inventory of shoe sizes mapped to their stock count
    shoe_sizes = Counter(map(int, input().split()))
    
    # Number of customers
    n = int(input())
    
    total_earned = 0
    
    for _ in range(n):
        size, price = map(int, input().split())
        
        # Check if the desired shoe size is in stock
        if shoe_sizes[size] > 0:
            total_earned += price
            shoe_sizes[size] -= 1  # Reduce stock after purchase
            
    print(total_earned)

