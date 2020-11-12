"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
"""

#solution
nums1 = [int(x) for x in input().split()]
nums2 = [int(y) for y in input().split()]


print(list(set(nums1) & set(nums2)))