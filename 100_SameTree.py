# Definition for a binary tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for the solution
class Solution:
	def isSameTree(self,p,q):
		#x is a TreeNode input
		# the first three conditions were all base conditions
		#condition 1: both empty
		if not p and not q:
			return True
		#condition 2: only one empty
		elif not p or not q:
			return False
		#non empty: compare the value, not equal
		if p.val != q.val:
			return False
		#else
		return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

	# the last two conditions could be merged together 99.17%
	    def isSameTree2(self, p: TreeNode, q: TreeNode) -> bool:
        if q == None and p == None:
            return True
        elif q == None or p == None:
            return False
        return q.val == p.val and self.isSameTree(p.right, q.right) and self.isSameTree(p.left,q.left)

