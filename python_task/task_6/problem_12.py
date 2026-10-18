#Question12-
#Problem Name - Set .discard(), .remove() & .pop()
#HackerRank Link - https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem


#.remove(x)
#This operation removes element x from the set.
#If element x does not exist, it raises a KeyError.
#The .remove(x) operation returns None.


n = int(input())
s = set(map(int, input().split()))

N = int(input())
for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'pop':
        s.pop()
    elif cmd[0] == 'remove':
        s.remove(int(cmd[1]))
    else:
        s.discard(int(cmd[1]))

print(sum(s))

  

