#Question19-
#Problem Name - Merge the Tools!
#HackerRank Link - https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        block = string[i:i + k]
        # In Python 3.7+, dict preserves insertion order and eliminates duplicates in O(k) time
        print("".join(dict.fromkeys(block)))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

