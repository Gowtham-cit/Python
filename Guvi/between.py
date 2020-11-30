n = int(input())
a, b = map(int,input().split())
if ((n < a and n > b ) or (n > a and n < b)):
    print("yes")
else:
    print("no")
