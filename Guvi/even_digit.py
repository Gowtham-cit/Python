n = int(input())
a = 0
for i in str(n):
    i = int(i)
    if i%2==0:
        a+=i

if a ==0:
    print("O")
else:
    print("E")
