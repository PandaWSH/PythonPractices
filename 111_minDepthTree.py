class Solution:
	# dfs
	def minDepth(self,root):
		if not root:
			return 0
		left = self.minDepth(root.left)
		right = self.minDepth(root.right)
		'''
		note: if the minimum didnt exist, that means the leftchild/rightchild 
		doesnt exsit of that node, so it should return the length of another 
		branch.
		'''
		return (min(left,right) or max(left,right)) + 1


	# bfs shared online
	'''
	In this BFS solution. It used depth as a global variable to track the current depth of the node. 
	Once It find that this node is a lead node, It can directly return current depth, which is exactly the result
	'''
	from collections import deque
	def minDepth(self,root):
		if not root:
			return 0

		queue = deque([root])
		depth = 1 # starting with depth == 1

		while queue:
			length = len(queue)
			for i in range(length):
				node = queue.popleft()
				if not node.left and not node.right:
					return depth

				if node.left:
					queue.append(node.left)

				if node.right:
					queue.append(node.right)

			depth += 1


