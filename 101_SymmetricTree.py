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

# second time - stack 36ms + 13.2MB (90.88% + 44.39%)
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        leftt = root.left
        rightt = root.right
        
        if not leftt and not rightt:
            return True
        elif not leftt or not rightt:
            return False
        elif leftt and rightt:
            return self.helper(leftt,rightt) # 一定要return，不能只写self.helper
        else:
            return True
        
    def helper(self, p, q):
        stack = [(p, q)]
        while stack:
            n1, n2 = stack.pop()
            
            if n1 and n2:
                if n1.val != n2.val:
                    return False
                stack += [(n1.right, n2.left), (n1.left, n2.right)] #关键
            elif n1 or n2:
                return False
            else:
                continue # 关键，不能在这时return false，因为有可能stack还没有空
        return True

# second time - 40ms + 13.3MB (74.15% + 24.84%)
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        def helper(self,p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val == q.val and helper(self,p.left,q.right) and helper(self,p.right,q.left)
        
        if not root:
            return True        
        return helper(self,root.left,root.right)
                
        