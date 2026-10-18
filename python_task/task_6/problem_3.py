#Question3-
#Problem Name - Python: Division
#HackerRank Link -https://www.hackerrank.com/challenges/python-division/problem

#The provided code stub reads two integers, a and b, from STDIN.
# Add logic to print two lines. The first line should contain the result of integer division,  a//b. The second line should contain the result of float division,  a/b .
#  No rounding or formatting is necessary.

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
# Integer division (floor division)
    print(a // b)
    
    # Float division
    print(a / b)


