#Given a number N, check if N is divisible by any number less than N other than 1.py
n = int(input())
count = 0

for i in range(2,n):
    if n%i == 0:
        count += 1
if count > 0:
    print("yes")
else:
    print("no")
