class Solution
	'''
	premise: the binary tree is height-balanced, 
	the depth of two subtrees never differ by more than 1 
	'''

	#methd one -- recursive (It's like up-down) 60ms + 15.5 MB (94.31% + 69.49%)
	def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        
        mid = len(nums) // 2
        
        root = TreeNode(nums[mid])
        
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root