'''

Given an unsorted integer array, find a pair with the given sum in it.

• Each input can have multiple solutions. The output should match with either one of them.

Input : nums[] = [8, 7, 2, 5, 3, 1], target = 10
Output: (8, 2) or (7, 3)

• The solution can return pair in any order. If no pair with the given sum exists, the solution should return an empty tuple.

Input : nums[] = [5, 2, 6, 8, 1, 9], target = 12
Output: ()

'''

class Solution:
	def findPair(self, nums: List[int], target: int) -> Tuple[int]:
		if len(nums) == 0 or len(nums) == 1:
			return ()
		# Write your code here...
		for i in range(len(nums)):
			j = i + 1
			while j < len(nums):
				temp = nums[i] + nums[j]
				if temp == target:
					return (nums[i], nums[j])
				j = j + 1
		return ()
