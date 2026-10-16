#Question14-
#Problem Name - Set .add()
#HackerRank Link - https://www.hackerrank.com/challenges/py-set-add/problem

#Apply your knowledge of the .add() operation to help your friend Rupal.
# Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of N country stamps.
# Find the total number of distinct country stamps.
#  Input Format
#   The first line contains an integer N, the total number of country stamps.
#    The next N lines contains the name of the country where the stamp is from.

if __name__ == '__main__':
    n = int(input())
    stamps = set()
    
    for _ in range(n):
        stamps.add(input())
        
    print(len(stamps))
