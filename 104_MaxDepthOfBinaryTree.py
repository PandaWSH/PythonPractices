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
        origin = [root]
        height = 0
        while set(origin) != {None}:
            height += 1
            queue = []
            for o in origin:
                if o is not None:
                    queue.append(o.left)
                    queue.append(o.right)
            origin = queue
        return height

    # second time - iteration solution
    def maxDepth(self, root):
        # Runtime: 36 ms, faster than 41.30% Memory Usage: 14.4 MB, less than 5.14%
        stack = []        
        if root is not None:
            stack.append((1, root))
        
        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))     
        return depth

    # second time - DFS iterative solution 没有完全想通
    def maxDepth(self, root):
        depth = 0 # initialize depth
        if not root:
            return depth
        stack = []
        value = []
        stack.append(root)
        value.append(depth + 1)
        while stack:
            node = stack.pop()
            temp = value.pop()
            depth = max(temp, depth)
            if node.right:
                stack.append(node.right)
                value.append(temp + 1)
            if node.left:
                stack.append(node.left)
                value.append(temp + 1)
        return depth





