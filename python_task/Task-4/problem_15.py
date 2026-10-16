#Question15-
#Problem Name - Word Order
#HackerRank Link - https://www.hackerrank.com/challenges/word-order/problem

#You are given N words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

if __name__ == '__main__':
    n = int(input())
    word_counts = {}
    
    for _ in range(n):
        word = input().strip()
        word_counts[word] = word_counts.get(word, 0) + 1
        
    # Line 1: Number of distinct words
    print(len(word_counts))
    
    # Line 2: Occurrence counts in order of appearance
    print(*word_counts.values())
