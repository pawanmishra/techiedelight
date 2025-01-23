'''

Given an integer array, return all equilibrium index in it. For an array `A[0..n-1]`, index `i` is an equilibrium index if the sum of elements of subarray `A[0…i-1]` is equal to the sum of elements of subarray `A[i+1…n-1]`.

Input : [0, -3, 5, -4, -2, 3, 1, 0]
Output: {0, 3, 7}
Explanation: For each index `i` in the output, A[0] + A[1] + … + A[i-1] = A[i+1] + A[i+2] + … + A[n-1]

Input : [-7, 3, 7, -3, 1]
Output: {4}
Explanation: `n-1` is an equilibrium index if A[0] + A[1] + … + A[n-2] sums to 0.

Input : [1, 2, -4, 2]
Output: {0}
Explanation: 0 is an equilibrium index if A[1] + A[2] + … + A[n-1] sums to 0.

'''

class Solution:
	def findEquilibriumIndex(self, nums: List[int]) -> Set[int]:
		indices = set()
		
		# Write your code here...
		for i in range(len(nums)):
			left_sum = 0
			right_sum = 0
			if i == 0:
				left_sum = 0
			if i == len(nums):
				right_sum = 0
			for j in range(0, i):
				left_sum += nums[j]
			for k in range(i + 1, len(nums)):
				right_sum += nums[k]
			
			if left_sum == right_sum:
				indices.add(i)
		return indices

