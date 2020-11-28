"""
https://leetcode.com/problems/linked-list-cycle-ii/
"""
 
#solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        ans = set()
        
        node = head
        
        while node:
            if node in ans:
                return node
            ans.add(node)
            
            node = node.next
        return None
 
