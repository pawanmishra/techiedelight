'''

Given an integer array, find a pair with the maximum product in it.

Each input can have multiple solutions. The output should match with either one of them.

Input : [-10, -3, 5, 6, -2]
Output: (-10, -3) or (-3, -10) or (5, 6) or (6, 5)

Input : [-4, 3, 2, 7, -5]
Output: (3, 7) or (7, 3)

If no pair exists, the solution should return an empty tuple.

Input : [1]
Output: ()

'''

class Solution:
	def findPair(self, nums: List[int]) -> Tuple[int]:
		if len(nums) == 0 or len(nums) == 1:
			return ()
		# Write your code here...
		max_sum = nums[0] * nums[1]
		ans_tuple = ()
		for i in range(len(nums)):
			j = i + 1
			while j < len(nums):
				temp = nums[i] * nums[j]
				if temp >= max_sum:
					max_sum = temp
					ans_tuple = (nums[i], nums[j])
				j = j + 1
		return ans_tuple

