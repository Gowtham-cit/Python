"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""


#code starts here
strs = input().split()   #user input list

size = len(strs)  #size of the list
if size == 0: return "" #if the size is 0 then print ""
if size == 1: return strs[0] #if the list have only one string then prints that alone

#list size > 1
strs.sort() #ordered list

end = min(len(strs[0]), len(strs[size - 1]))

i =0
while (i < end and strs[0][i] == strs[size - 1][i]):
    i += 1
pre = strs[0][0:i]

return pre
#code ends here
