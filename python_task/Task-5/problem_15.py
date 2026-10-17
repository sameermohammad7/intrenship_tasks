#Question15-
#Problem Name - Lists
#HackerRank Link - https://www.hackerrank.com/challenges/python-lists/problem

#Consider a list (list = []). You can perform the following commands:
# insert i e: Insert integer e at position i.
#  print: Print the list.
#   remove e: Delete the first occurrence of integer .
#    append e: Insert integer e at the end of the list.
#     sort: Sort the list.
#      pop: Pop the last element from the list.
#       reverse: Reverse the list.
#        Initialize your list and read in the value of n followed by n lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.


  if __name__ == '__main__':
    N = int(input())
    res = []
    
    for _ in range(N):
        command = input().split()
        cmd_type = command[0]
        
        if cmd_type == 'insert':
            res.insert(int(command[1]), int(command[2]))
        elif cmd_type == 'print':
            print(res)
        elif cmd_type == 'remove':
            res.remove(int(command[1]))
        elif cmd_type == 'append':
            res.append(int(command[1]))
        elif cmd_type == 'sort':
            res.sort()
        elif cmd_type == 'pop':
            res.pop()
        elif cmd_type == 'reverse':
            res.reverse()
