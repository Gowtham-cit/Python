n=int(input())
a=input()
b=input()
l=[]
for i in a:
    if i in b:
        l.append(i)

for i in a:
    if i not in b:
        x=a.index(i)
        break
for i in l:
    print(*a[0:x],sep="")
    break
        

        

        
        
            
    
    
