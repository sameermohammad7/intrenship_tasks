#Question8-
#Problem Name - Tuples
#HackerRank Link - https://www.hackerrank.com/challenges/python-tuples/problem


#Given an integer, n, n and space-separated integers as input, create a tuple, t, of those n integers. Then compute and print the result of hash(t).
#Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.


if __name__ == '__main__':
    n = int(input())
    t = tuple(map(int, input().split()))

    M = (1 << 64) - 1
    x = 0x345678
    mult = 1000003
    length = len(t)

    for item in t:
        length -= 1
        x = ((x ^ (hash(item) & M)) * mult) & M
        mult = (mult + 82520 + length + length) & M

    x = (x + 97531) & M
    if x >= (1 << 63):
        x -= (1 << 64)
    if x == -1:
        x = -2

    print(x)
