"""
https://www.hackerrank.com/challenges/python-sort-sort/problem
"""

#solution

#solution
n, m = map(int, input().split())
lst = [list(map(int, input().split())) for i in range(n)]
k = int(input())

lst.sort(key = lambda x: x[k])

for ans in lst:
    print(*ans)
