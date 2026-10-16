#Question20-
#Problem Name - No Idea!
#HackerRank Link - https://www.hackerrank.com/challenges/no-idea/problem

#There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. For each integer in the array, if i E A, you add 1 to your happiness. If 1 E B, you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

if __name__ == '__main__':
    # Read n and m
    n, m = map(int, input().split())
    
    # Read the array of integers
    arr = list(map(int, input().split()))
    
    # Read set A and set B as Python sets for O(1) lookup
    set_a = set(map(int, input().split()))
    set_b = set(map(int, input().split()))
    
    happiness = 0
    
    # Iterate through the array and update happiness
    for num in arr:
        if num in set_a:
            happiness += 1
        elif num in set_b:
            happiness -= 1
            
    print(happiness)
