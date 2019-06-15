class Solution:
	#method 1, recursive BFS 52ms + 15.1 MB(75.64% + 76.88%)
	def hasPathSum(self,root,sum):
		#if the root it zero
		if not root:
			return False
		if not root.left and not root.right and root.val == sum:
			return True
		if root.left:
			# update the value of sum to sum-root.val, which is the prev root
			left = self.hasPath(root.left, sum-root.val)
		if root.right:
			right = self.hasPath(root.right, sum-root.val)
		return True if left or rifht else False

	# method 2, iterative DFS (40ms + 15.2 MB, 99.36% + 54.40%)
	def hasPathSum(self,root,sum):
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True
        stack = [(root,root.val)]
        while stack:
            cur,cur_val = stack.pop()
            if not cur: #not neccessary
                return False
            if not cur.left and not cur.right and cur_val == sum:
                return True
            if cur.left:
                stack.append((cur.left, cur_val + cur.left.val))
            if cur.right:
                stack.append((cur.right, cur_val + cur.right.val))
        return False