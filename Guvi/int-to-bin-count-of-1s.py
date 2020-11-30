def int_bin(n):
    x = "{0:b}".format(n)
    x = str(x)
    count = 0
    for i in x:
        if i == '1':
            count += 1
            
    print(count)
n = int(input())
int_bin(n)
