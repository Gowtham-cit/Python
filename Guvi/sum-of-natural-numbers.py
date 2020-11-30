def naturalsum(n):
    sum = 0
    for i in range(0, n+1, 1):
        sum = sum + i
    print(sum)
n = int(input())
naturalsum(n)
