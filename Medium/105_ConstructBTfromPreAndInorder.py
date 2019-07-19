# online method 60ms + 15MB (79.63% + 95.44%)
class Solution:
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        root = TreeNode(0)
        lo, hi = 0, len(preorder) - 1
        nodes = [(root, lo, hi)]
        lut = {inorder[i]: i for i in range(len(inorder))} 
              # use a look up table to get the index
              # of an element in constant time.
        for i in range(len(preorder)):
            curr, lo, hi = nodes.pop()
            curr.val = preorder[i]
            mid = lut[curr.val]
            if mid < hi:
                curr.right = TreeNode(0)
                nodes.append((curr.right, mid + 1, hi))
            if lo < mid:
                curr.left = TreeNode(0)
                nodes.append((curr.left, lo, mid - 1))
        return root