"""
https://leetcode.com/problems/reverse-only-letters
"""
#solution
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        
        S = list(S)
        l, r = 0, len(S)-1
        
        while l < r:
            if not S[l].isalpha():
                l += 1
            elif not S[r].isalpha():
                r -= 1
            else:
                S[l], S[r] = S[r], S[l]
                l += 1
                r -= 1
                
        return ''.join(S)

"""
#solution
S = input()
S = list(S)
l, r = 0, len(S)-1
while l < r:
    if not S[l].isalpha():
        l += 1
    elif not S[r].isalpha():
        r -= 1
    else:
        S[l], S[r] = S[r], S[l]
        l += 1
        r -= 1
print(''.join(S))

#TEST CASE 1:
input : ab_cd
output: dc_ba

#TEST CASE 2:
input: Gow*th-a_m
output: mah*tw-o_G
"""
