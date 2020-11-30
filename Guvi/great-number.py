n = input()
l = []
product = 1
for i in n:
    a = int(i)
    l.append(a)
for i in l:
    product = product * i
if int(n) == sum(l) + product:
    print("Great")
else:
    print("not")
    

