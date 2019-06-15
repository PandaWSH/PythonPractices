class Solution:
	# 64ms + 18.1 MB (58.63% + 43.52%)
	def isBalanced(self.root):
		if not root:
			return True
		elif self.helper(root) == -1:
			return False
		else:
			return True

	def helper(self,root):
		if not root:
			return 0

		left = self.helper(root.left)
		right = self.helper(root.right)

		if left == -1 or right == -1 or abs(left-right) > 1:
			return -1

		return max(left,right) + 1
# method 2 (60ms + 18.7 mb)
# note: a method within a method
class Solution:
	def isBalanced(self,root):
		def helper(root):
			if not root
				return 0
			else:
				left = helper(root.left)
				right = helper(root.right)
				if left == -1 or right == -1 or abs(left - right) > 1:
					return -1
				return max(left,right) + 1

		return helper(root) != -1