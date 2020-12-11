#sum of the elements of set 
#py-set-discard-remove-pop
n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    x = input().split()
    if x[0] == "pop":
        s.pop()
    elif x[0] == "remove":
        s.remove(int(x[1]))
    elif x[0] == "discard":
        s.discard(int(x[1]))
        
print(sum(s))
