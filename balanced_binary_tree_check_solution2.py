# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return -1 != self.helper(root)
        
    def helper(self,node):
        if not node:
            return 0
        else:
            l = self.helper(node.left)
            if l == -1:
                return -1
            r = self.helper(node.right)
            if r == -1:
                return -1
            if abs(l-r)>1:
                return -1
            return max(l,r)+1