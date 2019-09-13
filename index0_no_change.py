s=input().split()
l=[]
for i in s:
    a=i[::-1]
    l.append(a)
l[0]=s[0]
print(*l)

