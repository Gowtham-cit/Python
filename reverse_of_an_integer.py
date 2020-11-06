#Reverse of an integer

integer = int(input()) #getting user input

#for positive integer(>0)
if integer > 0:          
    print(int(str(integer)[::-1]))

#for negative integer
if integer < 0:
    print(-1 * int(str(integer * -1)[::-1]))
