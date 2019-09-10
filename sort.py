n=int(input())
l=list(map(int,input().split()))
flag=0
i=1
while i< len(l):
    if(l[i]<l[i-1]):
       flag=1
    i+=1
if (not flag):
    print("yes")
else:
    print("no")
    
