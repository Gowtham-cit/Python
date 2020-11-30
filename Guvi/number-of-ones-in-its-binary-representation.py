a, b = map(int,input().split())
a ^= b
a = bin(a)
s = str(a)
count = 0
for i in s:
    if i == '1':
        count += 1
print(count)

