"""
https://leetcode.com/problems/power-of-two/
""""
#solution
n = int(input())
print(n>0 and bin(n).count('1') == 1)

"""
Trace if n = 16
if n = 16 then n>o becomes True  and bin(16) = 10000 
here count of 1 will one so
bin(16).count('1') == 1 also True

It will return True
"""
