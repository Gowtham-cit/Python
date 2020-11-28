"""
https://www.hackerrank.com/challenges/any-or-all/problem
"""

#solution
def ans():
    n = int(input())
    lst = [str(x) for x in input().split()]
    if all(map(lambda x: int(x)>0,lst)) and any([j == j[::-1] for j in lst]) : return True
    else: return False
print(ans())
