'''

Given an integer array of size `n`, return the element which appears more than `n/2` times. Assume that the input always contain the majority element.

Input : [2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2]
Output: 2

Input : [1, 3, 1, 1]
Output: 1

'''

class Solution:
	def findMajorityElement(self, nums: List[int]) -> int:
		dict = {}
		nums_size = len(nums) / 2
		for num in nums:
			if num in dict:
				dict[num] += 1
			else:
				dict[num] = 1
		for key, value in dict.items():
			if value >= nums_size:
				return key
		# Write your code here...
		return
