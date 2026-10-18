#Question17-
#Problem Name - Check Strict Superset
#HackerRank Link - https://www.hackerrank.com/challenges/py-check-strict-superset/problem


#You are given a set A and n other sets.
#Your job is to find whether set A is a strict superset of each of the n sets.
#Print True, if A is a strict superset of each of the N sets. Otherwise, print False.
#A strict superset has at least one element that does not exist in its subset.


# Read the main set A
set_a = set(map(int, input().split()))

# Read the number of other sets
n = int(input())

# Check whether set_a is a strict superset of all other given sets
is_strict_superset = True

for _ in range(n):
    other_set = set(map(int, input().split()))
    # A strict superset must strictly contain the other set (i.e., set_a > other_set)
    if not (set_a > other_set):
        is_strict_superset = False
        break

print(is_strict_superset)
