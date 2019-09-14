n=input()
a=0
for i in n:
    i=int(i)
    a+=i
a=str(a)
if a==a[::-1]:
    print("yes")
else:
    print("no")
	
