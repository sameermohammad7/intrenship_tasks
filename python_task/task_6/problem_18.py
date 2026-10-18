#Question18-
#Problem Name - Set Mutations
#HackerRank Link - https://www.hackerrank.com/challenges/py-set-mutations/problem


#You are given a set A and N number of other sets. These N number of sets have to perform some specific mutation operations on set A.
#Your task is to execute those operations and print the sum of elements from set A.

# Read the number of elements and the base set
n = int(input())
base_set = set(map(int, input().split()))

# Read the number of operations
num_operations = int(input())

# Process each mutation operation
for _ in range(num_operations):
    op_name = input().split()[0]
    other_set = set(map(int, input().split()))
    
    # Dynamically call the mutation method (e.g., update, intersection_update, etc.)
    getattr(base_set, op_name)(other_set)

# Print the sum of the remaining elements
print(sum(base_set))
