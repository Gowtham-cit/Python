
'''Anna and Brian order n items at a restaurant
but Anna declines to eat any of the kth item due to an allergy.
When the check comes, they decide to split the cost of all the items
they shared; however, Brian may have forgotten that they didnt 
split the kth item and accidentally charged Anna for it.
You are given n,k the cost of each of the n items, and the total amount of money that Brian charged Anna for her portion of the bill
If the bill is fairly split, print    Bon Appetit otherwise, print the amount of money that Brian must refund to Anna '''

 #user input
n, k = map(int,input().split())
l = [int(x) for x in input().split()]

#code goes here
l.remove(l[k])
m = int(input())
s= sum(l)
d= s//2

#if the value of d == m then it will Bon Appetit else the difference between m and d
if d == m:
 print("Bon Appetit")
else:
 print(m-d)
