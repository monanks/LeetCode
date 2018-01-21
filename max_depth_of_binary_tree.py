# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            return self.helper(root,0)
    
    def helper(self,node,height):
        if not node:
            return height
        else:
            return max(self.helper(node.left,height+1),self.helper(node.right,height+1))