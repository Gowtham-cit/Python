"""
https://www.hackerrank.com/challenges/balanced-brackets/problem
"""
#solution
#!/bin/python3

import os

import sys

# Complete the isBalanced function below.
def isBalanced(s):
    n = -1
    while len(s) != n:
        n = len(s)
        s = s.replace("()", "")
        s = s.replace("[]", "")
        s = s.replace("{}", "")
    if len(s) == 0:
        return "YES"
    else:
        return "NO"
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
