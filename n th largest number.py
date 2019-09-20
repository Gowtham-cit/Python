n,k = input().split()
n=int(n)
k=int(k)
lst=[int(x) for x in input().split()]
lst.sort()
print(lst[-k])
