#Question8-
#Problem Name - What's Your Name?
#HackerRank Link - https://www.hackerrank.com/challenges/whats-your-name/problem


#Complete the print_full_name function in the editor below.
# print_full_name has the following parameters:
#  string first: the first name
#   string last: the last name
#    Prints
#     string: 'Hello firstname lastname! You just delved into python' where firstname and lastname are replaced with first and last.

#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

