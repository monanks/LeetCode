# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        node = root
        max  = 0
        q = [root]
        
        while q:
            t = q.pop()
            temp = self.helper(t.left) + self.helper(t.right)
            if temp > max:
                max = temp
            if t.left:
                q.insert(0,t.left)
            if t.right:
                q.insert(0,t.right)
            
        return max
        
    def helper(self,node):
        if not node:
            return 0
        else:
            return max(self.helper(node.left),self.helper(node.right))+1