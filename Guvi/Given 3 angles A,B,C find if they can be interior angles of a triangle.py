#Given 3 angles A,B,C find if they can be interior angles of a triangle
a, b, c = map(int,input().split())
if (a + b + c == 180):
    print("yes")
else:
    print("no")
