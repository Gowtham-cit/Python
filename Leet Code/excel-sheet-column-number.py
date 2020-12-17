class Solution:
    def titleToNumber(self, s: str) -> int:
        
        r, count = len(s)-1, 0
        
        c = 0
        
        
        #To get  A -> 1 B -> 2 C -> 3 ....... Z -> 26
        #example D -> 4
        #To get 4 
        #ord('D') - ord('A') + 1 = 4
        #Here ord() will return ascii value of char
        def getNumber(char):
            return ord(char) - ord('A') + 1 
        
        
        #Iteration for all char in s
        for char in s:
            c += pow(26, r) * getNumber(char)
            r -= 1
        return c
        """
        Trace for AB

        char ->A
        c += pow(26, 1) *getNumber(A)
        c = 26 * 1

        c = 26    #c += pow(26, r) * getNumber(char)

        r = 2 - 1

        nxt char - > B

        c += pow(26, 0) * getNumber(A)
        c = 1 * 2
        c = 2
        so c = 26 + 2 #c += pow(26, r) * getNumber(char)
             c = 28

        r = 1 - 1 = 0

        """
