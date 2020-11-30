"""
https://www.hackerrank.com/challenges/nested-list/problem
"""
#solution

lst = [[input(), float(input())] for _ in range(int(input()))]

names, scores = [], set()

for name, score in lst:
    
    names.append(name)
    scores.add(score)

second_lowest_grade = sorted(scores)[1]

for name, score in sorted(lst):
    
    if second_lowest_grade == score:
        print(name)
