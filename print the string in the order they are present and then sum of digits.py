s=input()
s1=""
plus=0
for i in s:
    if i.isdigit():
        i=int(i)
        plus+=i
    else:
        s1+=i
print(s1+str(plus))
        
