'''

Given the root of a binary tree, return the left view of its nodes' values. Assume the left and right child of a node makes a 45–degree angle with the parent.

Input:
		   1
		 /	 \
		/	  \
	   2	   3
	  		 /   \
	 	  	/	  \
		   5	   6
		 /   \
		/	  \
	   7	   8

Output: [1, 2, 5, 7]

Input:

	  1
	/   \
   /	 \
  2		  3
   \	 /
	\   /
	 4 5

Output: [1, 2, 4]

'''

class Solution:

	'''
	A binary tree node is defined as:

	class Node:
		def __init__(self, data=None, left=None, right=None):
			self.data = data	# data field
			self.left = left	# pointer to the left child
			self.right = right	# pointer to the right child
	'''

	def findLeftView(self, root: Node) -> List[int]:
		view = []
		aux = []
		if root:
			aux.append(root)
		while aux:
			view.append(aux[0].data)
			temp_aux = []
			for item in aux:
				if item.left:
					temp_aux.append(item.left)
				if item.right:
					temp_aux.append(item.right)
			aux = temp_aux
		
				
		# Write your code here...
		return view

