def gcd(a,b):
    for i in range(1,min(a,b)+1):
        if (a%i==0 and b%i==0):
            mrcf=i
    return mrcf
a,b=map(int,input().split())
print(gcd(a,b))
