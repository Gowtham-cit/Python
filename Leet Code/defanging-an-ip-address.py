"""
https://leetcode.com/problems/defanging-an-ip-address/
"""
#solution

class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        adress = address.replace(".", "[.]")
        
        return adress
