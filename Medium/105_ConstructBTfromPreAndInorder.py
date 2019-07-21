# online method 60ms + 15MB (79.63% + 95.44%)
class Solution:
    def buildTree(self, preorder, inorder):
    # given a preorder and an inorder BT
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


# From @JieGhost 60ms + 14.6MB
class Solution(object):
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None
            
        head = TreeNode(preorder[0])
        stack = [head]
        i = 1
        j = 0
        
        while i < len(preorder):
            temp = None
            t = TreeNode(preorder[i])
            while stack and stack[-1].val == inorder[j]:
                temp = stack.pop()
                j += 1
            if temp:
                temp.right = t
            else:
                stack[-1].left = t
            stack.append(t)
            i += 1        
        return head

#https://leetcode-cn.com/problems/two-sum/solution/cong-qian-xu-he-zhong-xu-bian-li-xu-lie-gou-zao-er/
#64ms + 18.8MB
class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def helper(in_left = 0, in_right = len(inorder)):
            nonlocal pre_idx
            # if there is no elements to construct subtrees
            if in_left == in_right:
                return None
            
            # pick up pre_idx element as a root
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)

            # root splits inorder list
            # into left and right subtrees
            index = idx_map[root_val]

            # recursion 
            pre_idx += 1
            # build left subtree
            root.left = helper(in_left, index)
            # build right subtree
            root.right = helper(index + 1, in_right)
            return root
        
        # start from first preorder element
        pre_idx = 0
        # build a hashmap value -> its index
        idx_map = {val:idx for idx, val in enumerate(inorder)} 
        return helper()

