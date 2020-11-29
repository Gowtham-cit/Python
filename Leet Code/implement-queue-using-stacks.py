"""
https://leetcode.com/problems/implement-queue-using-stacks/
"""
#solution
class MyQueue:

    def __init__(self):
        
        self.queue = [] #creating an empty list(Queue)
        

    def push(self, x: int) -> None:
        
        self.x = x
        self.queue.append(self.x) #adding an element using append

    def pop(self) -> int:
        
        return self.queue.pop(0) #Removing the first element using pop(0)

    def peek(self) -> int:
        
        return self.queue[0] #first element in the Queue
    
    def empty(self) -> bool:
        
        return len(self.queue) == 0 #if Queue is empty
