#Question7-
#Problem Name - Alphabet Rangoli
#HackerRank Link - https://www.hackerrank.com/challenges/alphabet-rangoli/problem

#You are given an integer, N. Your task is to print an alphabet rangoli of size N.(Rangoli is a form of Indian folk art based on creation of patterns.)


import string

def print_rangoli(size):
    alphabet = string.ascii_lowercase
    lines = []
    
    # Generate the top half including the center row
    for i in range(size):
        # Slice letters from size-1 down to i, then mirror back
        left_side = alphabet[size - 1 : i : -1]
        right_side = alphabet[i : size]
        row_chars = left_side + right_side
        
        # Join with '-' and center pad with '-'
        lines.append("-".join(row_chars).center(4 * size - 3, "-"))
    
    # Bottom half is the reverse of top half (excluding middle row)
    full_pattern = lines[::-1] + lines[1:]
    print("\n".join(full_pattern))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
