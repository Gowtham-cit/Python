
def insertion_sort(lst):
        for i in range(1, len(lst)):
                
                current_element = lst[i]
                position = i
                
                while current_element < lst[position - 1] and position > 0:
                        lst[position] = lst[position - 1]
                        position = position -1
                        lst[position] = current_element
                        #print(lst)  #each step
                #print(lst) #each step final answer
        return lst
lst = [int(x) for x in input().split()]
print(insertion_sort(lst))

"""
input: 5 4 3 2 1
output: [1, 2, 3, 4, 5]
"""
