n = int(input())
l = [int(x) for x in input().split()]


 #creting a empty list to store subarrays 
sublst = []   
for i in range(n+1):
    for j in range(i+1,n+1):
        sub = l[i:j]            #subarray of list l
        sublst.append(sub)    #appending sub list 


ans = []
for i in sublst:
    if sorted(i) == list(range(min(i), max(i)+1)) :
        ans.append(len(i))
print(max(ans))
  

