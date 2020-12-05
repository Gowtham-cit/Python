"""
https://www.guvi.in/code-kata-main?concept=searching
"""
#solution
t = int(input())
for i in range(t):
    l = list(map(int,input().split()))
    j = 1
    while(l[1]**j<=l[0]):
        j+=1
    print(l[1]**(j-1))
