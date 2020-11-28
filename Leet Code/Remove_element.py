"""
https://leetcode.com/problems/remove-element/
""""
#solution

nums = [int(x) for x in input().split()]
value = int(input())

while(value in nums):
  del nums[nums.index(value)]
print(len(nums))

#print(nums) #to print the list
