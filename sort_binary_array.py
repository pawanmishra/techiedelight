'''

Given a binary array, in-place sort it in linear time and constant space. The output should contain all zeroes, followed by all ones.

Input : [1, 0, 1, 0, 1, 0, 0, 1]
Output: [0, 0, 0, 0, 1, 1, 1, 1]

Input : [1, 1]
Output: [1, 1]

'''

class Solution:
	def sortArray(self, nums: List[int]) -> None:
		# Write your code here...
		num_of_zeros = 0
		for i in range(len(nums)):
			if nums[i] == 0:
				num_of_zeros += 1
			nums[i] = 1
		for i in range(num_of_zeros):
			nums[i] = 0
		return
