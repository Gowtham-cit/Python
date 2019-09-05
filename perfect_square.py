import math 

def isPerfectSquare(x,y):
    z=x*y
    sr = math.sqrt(z)  
    return ((sr - math.floor(sr)) == 0) 



x, y = map(int,input().split())
if (isPerfectSquare(x,y)): 
	print("yes") 
else: 
	print("no") 

