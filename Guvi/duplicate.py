from collections import Counter
def duplicate(a):
    c=Counter(str(a))
    if any(value>1 for value in c.values()):
        print("yes")
    else:
        print("no")
a=int(input())
duplicate(a)
