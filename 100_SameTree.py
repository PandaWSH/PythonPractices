# Definition for a binary tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# second time - 32ms + 13.1MB [90.67% + 65.35%]
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

        '''
        if the last three lines wrote as:
        else:
            if p.val != q.val:
                return False
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        the entire program would be much slower
        '''

	# the last two conditions could be merged together 99.17%
	    def isSameTree2(self, p: TreeNode, q: TreeNode) -> bool:
        if q == None and p == None:
            return True
        elif q == None or p == None:
            return False
        return q.val == p.val and self.isSameTree(p.right, q.right) and self.isSameTree(p.left,q.left)

# flag method
class Solution:
    def __init__(self):
        self.flag = True
        
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None or q is None:
            if p != q:
                self.flag = False
        else:
            if p.val != q.val:
                self.flag = False
            Solution.isSameTree(self, p.left, q.left)
            Solution.isSameTree(self, p.right, q.right)
        return self.flag

# method 3 - similar to method one
    def isSameTree(self, p, q):
        if not p or not q:
            return p == q
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# method 4 DFS + stack
class Solution(object):
    def isSameTree(self, p, q):
        stack = [(q, p)]
        while stack:
            n1, n2 = stack.pop()
            
            if n1 and n2:
                if n1.val != n2.val:
                    return False
                stack += [(n1.right, n2.right), (n1.left, n2.left)]
            elif n1 or n2:
                return False
            else:
                continue
            
        return True
