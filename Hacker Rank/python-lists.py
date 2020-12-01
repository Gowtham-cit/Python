"""
https://www.hackerrank.com/challenges/python-lists/problem
"""
#solution

lst = []
for _ in range(int(input())):
    s = input().split()
    
    cmd = s[0]
    args = s[1:]
    
    if cmd !="print":
        
        cmd += "("+ ",".join(args) +")"
        eval("lst."+cmd)
    
    else:
        print(lst)
