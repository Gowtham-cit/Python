"""
https://leetcode.com/problems/happy-number/
"""

#solution
def happy(n):
    cnt = 0
       
    while True:
        nn = 0
        while n > 0:
            d = n % 10
            nn += d * d
            n //=10
        n = nn
        cnt += 1
            
        if nn == 1:
            return True
        if cnt > 11:
            return False
            
            
print(happy(int(input())))





