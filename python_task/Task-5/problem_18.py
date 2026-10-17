#Question18-
#Problem Name - The Minion Game
#HackerRank Link - https://www.hackerrank.com/challenges/the-minion-game/problem

#Kevin and Stuart want to play the 'The Minion Game'.
# Game Rules
#  Both players are given the same string, S.
#   Both players have to make substrings using the letters of the string S.
#    Stuart has to make words starting with consonants.
#      Kevin has to make words starting with vowels.
#       The game ends when both players have made all possible substrings.
#         Scoring
#          A player gets +1 point for each occurrence of the substring in the string S.

def minion_game(string):
    vowels = 'AEIOU'
    stuart_score = 0
    kevin_score = 0
    length = len(string)
    
    for i in range(length):
        # A character at index i can form (length - i) substrings starting at that index
        points = length - i
        
        if string[i] in vowels:
            kevin_score += points
        else:
            stuart_score += points
            
    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)

