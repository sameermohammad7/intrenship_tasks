#Question7-
#Problem Name - List Comprehensions
#HackerRank Link - https://www.hackerrank.com/challenges/list-comprehensions/problem


#This is HackerRank's List Comprehensions challenge.
#You need to print a list of all possible coordinates 
#$[i, j, k]$ on a 3D grid where $0 \le i \le x$, $0 \le j \le y$, $0 \le k \le z$, and the sum $i + j + k \ne n$.

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    result = [
        [i, j, k]
        for i in range(x + 1)
        for j in range(y + 1)
        for k in range(z + 1)
        if i + j + k != n
    ]
    
    print(result)

