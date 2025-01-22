'''

Given an integer array, in-place move all zeros present in it to the end. The solution should maintain the relative order of items in the array and should not use constant space.

Input : [6, 0, 8, 2, 3, 0, 4, 0, 1]
Output: [6, 8, 2, 3, 4, 1, 0, 0, 0]

'''

class Solution:
	def rearrange(self, nums: List[int]) -> None:
		k = 0
		# Write your code here...
		for i in range(len(nums)):
		    if nums[i]:
		        nums[k] = nums[i]
		        k = k + 1
		
		for k in range(k, len(nums)):
		    nums[k] = 0
		return

