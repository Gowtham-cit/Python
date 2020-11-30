#pyramid pattern
"""
Example
5
1 

1 1 1 

1 1 1 1 1 

1 1 1 1 1 1 1 

1 1 1 1 1 1 1 1 1 
"""
#solution
n=int(input())
k=1
for i in range(0,n):
    
    for j in range(0,k):
        print('1',end=" ")
    k+=2
        
    print("\r")
