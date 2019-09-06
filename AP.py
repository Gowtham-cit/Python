n=int(input())
x=[str(i) for i in input().split()]
count=0
for i in x:
    if i=="P":
        count+=1
if count<(n*0.25*count):
    print("Not Blacklisted")
else:
    print("Blacklisted")
    
