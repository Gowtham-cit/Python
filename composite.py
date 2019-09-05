def iscomposite(n):
    if n<=1:
        return False
    if n<=3:
        return False
    if n%2==0 or n%2==0:
        return True
    i=5
    while(i*i<=n):
        if(n%i==0 or n%(i+2)==0):
            return True
        i+=6
    return False
n=int(input())
print("yes") if(iscomposite(n)) else print("no")
