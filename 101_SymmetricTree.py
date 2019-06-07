# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # if it's empty, we take it as yes
        if root == None:
            return True
        #otherwise, compare the left and right sub-tree
        return self.helpSymmetric(root.left,root.right)

    #sub funtion, creating a and b, as p and q in question 100
    def helpSymmetric(self,a,b):
        #if both empty
        if not a and not b:
            return True
        #if there's one side with tree
        if not a or not b:
            return False
        return a.val == b.val and self.helpSymmetric(a.left,b.right) and self.helpSymmetric(a.right, b.left)