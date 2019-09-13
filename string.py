s=input()
n=len(s)
if n%2==0:
    n=n/2
    n=int(n)
    print(s[:n-1]+"**"+s[n+1:])
else:
    n=int(n/2+0.5)
    print(s[:n-1]+"*"+s[n:])
    
