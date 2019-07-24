# 107 second time, same method
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res,data=[],[]
        # empty
        if not root:return res 
        
        # non-empty
        stack=[]
        stack.append(root) #now stack has everything from the root
        
        nCount=1#记录每层节点数
        while stack:
            node=stack.pop(0) #recode the node and delete from stack
            data+=[node.val]#保存每层节点的值++
            nCount-=1
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            if nCount==0:
                res=[data]+res
                data=[]
                nCount=len(stack) #number of nodes left
        return res

#second method
class Solution(object):        
        def levelOrderBottom(self, root):
            if root is None:
                return []
            res = []
            self.dfs([root], res)
            return res
            
        def dfs(self, level_nodes, res):
            if not level_nodes: return
            res.insert(0, [])
            temp = []
            for node in level_nodes:
                res[0].append(node.val)
                if node.left: temp.append(node.left)
                if node.right: temp.append(node.right)
            self.dfs(temp, res)