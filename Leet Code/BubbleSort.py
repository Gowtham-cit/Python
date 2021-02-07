def BubbleSort(lst):

        n = len(lst)
        for i in range(n):
                
                for j in range(0,  n - i - 1):
                        
                        if lst[j] > lst[j+1]:
                                lst[j], lst[j+1] = lst[j+1], lst[j]
                        
                        
                
        print(lst) #final sortted array
#driver code        
lst =[int(x) for x in input().split()]

BubbleSort(lst)
