a, b = map(int,input().split())
l = list(map(int,input().split()))
g = list(map(int,input().split()))
for i in g:
    l.append(i)
    print(max(l), end=" ")

