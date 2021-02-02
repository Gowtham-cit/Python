"""
Test case 1:
input:
7
1 2 3 4 5 6 7 8 9
output:
1234321

Test case 2:
input:
6
1 2 3 4 5 6
output:
12444321

Test case 3:
input:
3
1 2 3
output:
121

"""
n = int(input())
l = [int(x) for x in input().split()]

if n % 2 ==1:
  s = ""
  for i in range(n//2+1):
    s+=str(l[i])
  for i in range(n//2-1,-1,-1):
    s+=str(l[i])
  print(s)
else:
  s = ""
  if l[n//2-1] >= l[n//2]:
    for i in range(n//2):
      s+=str(l[i])
    s+=s[::-1]
    print(s)
  else:
    for i in range(n//2 -1):
      s+=str(l[i])
    s += str(l[n//2])*2
    for i in range(n//2, -1,-1):
      s+=str(l[i])
    print(s)


