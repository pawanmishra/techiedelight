'''

Given two sorted integer arrays, `X[]` and `Y[]` of size `m` and `n` each, in-place merge elements of `X[]` with elements of array `Y[]` by maintaining the sorted order, i.e., fill `X[]` with the first `m` smallest elements and fill `Y[]` with remaining elements.

Input :

X[] = [1, 4, 7, 8, 10]
Y[] = [2, 3, 9]

Output:

X[] = [1, 2, 3, 4, 7]
Y[] = [8, 9, 10]

'''

class Solution:
	def merge(self, X: List[int], Y: List[int]) -> None:
		# Write your code here...
		len_x = len(X)
		len_y = len(Y)
		
		for i in range(len_x):
			xi = X[i]
			y0 = Y[0]
			
			if xi > y0:
				X[i] = y0
				Y[0] = xi
				
				# sort Y
				for j in range(1, len_y):
					if Y[j] < Y[j - 1]:
						temp = Y[j - 1]
						Y[j - 1] = Y[j]
						Y[j] = temp
		return
