n=int(input())
a=str(bin(n))
d=a.replace("0b","")
b=[]
for i in d:
    b.append(i)
c=b[::-1]
e=c.index('1')
print(e+1)
    
      
