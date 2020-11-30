string = input()
count1 = 0
count2 = 0
count3 = 0
count4 = 0 
count5 = 0
count6 = 0
for i in string:
    if i == "(":
        count1 += 1
    if i == ")":
    	count2 += 1
    if i == "[":
        count3 += 1
    if i == "]":
        count4 += 1
    if i == "{":
        count5 += 1
    if i == "}":
        count6 += 1
if count1 == count2 and count3 == count4 and count5 == count6:
    print("yes")
else:
    print("no")
