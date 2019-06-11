#Recursively DFS Solution
class Solution1:
    # 32ms + 14.7 (79.97% + 23.26%)
    # recursive method
    def maxDepth(self, root):
        if root is None: 
            return 0  #base case
        else:  #recur case
            left_height = self.maxDepth(root.left) 
            right_height = self.maxDepth(root.right) 
            return max(left_height, right_height) + 1 

    # 36ms + 14.7 MB (47.42% + 42.84%)
    def maxDepth(self, root):
        depth = 0
        level = [root] if root else []
        while level:
            depth += 1
            queue = []
            for el in level:
                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)
            level = queue          
        return depth

    # 24ms + 14.6MB (98.03% + 57.11%)
    def maxDepth(self, root):       
        # intertive solution
        ls = [root]
        depth = 0

        # when it's non-zero
        while set(ls) != {None}: 
            depth += 1
            # queue
            ls_ = []

            for l in ls:
                if l is not None:
                    ls_.append(l.left)
                    ls_.append(l.right)
            ls = ls_
        return depth