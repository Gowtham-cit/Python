def rotate_string(string, n):
    n = int(n)
    print("{}{}".format(string[n:], string[0:n]))
    
    
string, n = input().split()
rotate_string(string, n)
