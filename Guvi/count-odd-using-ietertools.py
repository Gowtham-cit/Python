from collections import Counter
n = int(input())
l = list(map(int,input().split()))
counter = Counter(l)
print(min(l, key = counter.get))
    
