'''You are given an array of N elements. Your task is to sort a subarray denoted by the index values i1 and i2 in descending order. Note: Index values start at 0. The sorting must be completed in O(i2-i1+1)log(i2-i1+1)
 

Input Description:
Size of array followed by elements of the array. The third line contains the start and end indices of the subarray( i1 and i2)

Output Description:
A partially sorted array'''

def partially_sort(l,a,b):

    ls = l[a:b+1]
    ls.sort(reverse=True)
    x = 0
    for i in range(a,b+1):
        l[i ]= ls[x]
        x += 1
    return l

#Driver code
n = int(input())
l = [int(x) for x in input().split()]
a, b = map(int,input().split())

print(*partially_sort(l, a, b))

