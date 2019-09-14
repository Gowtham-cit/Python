n=input()
l=[]
m=[]
for i in n:
    i=int(i)
    if i%2==0:
        l.append(i)
    else:
        m.append(i)
if len(n)==len(l):
    print(-1)
else:
    print(*m)
#if len(l)==len(n)
