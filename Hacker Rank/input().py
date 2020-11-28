"""
https://www.hackerrank.com/challenges/input/problem
"""
#solution
x, k = map(int, input().split())
print(eval(input()) == k)

"""
What is eval?
 ->eval is a built-in- function used in python, eval function parses the expression argument and evaluates it as a python expression. In simple words, the eval function evaluates the “String” like a python expression and returns the result as an integer.
Syntax

The syntax:
eval(expression, [globals[, locals]])

"""

