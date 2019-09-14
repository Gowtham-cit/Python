import math
x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
x4,y4=map(int,input().split())
d1=math.sqrt((x1-x2)**2+(y1-y2)**2)
d2=math.sqrt((x3-x4)**2+(y3-y4)**2)
if d1==d2:
    print("yes")
else:
    print("no")
