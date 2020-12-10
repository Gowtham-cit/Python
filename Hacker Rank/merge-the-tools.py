"""
https://www.hackerrank.com/challenges/merge-the-tools/problem
"""

#solution

def merge_the_tools(string, k):
    # your code goes here
    
    #number of outputs
    lnth = len(string)//k
    
    for i in range(lnth):
        
        #to remove duplicate in string[:k]
        t = "" 
        for i in string[:k]: 
            if(i in t): 
                pass
            else: 
                t=t+i 
        print(t)
        
        string = string[k:]
    
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
