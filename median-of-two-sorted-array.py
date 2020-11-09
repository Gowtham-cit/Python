"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000
Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

"""
#solution
#user input
nums1 = [int(x) for x in input().split()]
nums2 = [int(y) for y in input().split()] 

lst = nums1 + nums2 #meiging the lists
lst.sort() #sorting the arraay elements

x = int(len(lst)/2) #middle element index

if len(lst) % 2 == 0: #if length of the lst is even then if pary
        lst = lst[x] + lst[x -1]
        print(lst/2)
else:  #if the length of the lst is odd then else part
        print(lst[x])
