# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            return abs(self.sumHelper(root.left) - self.sumHelper(root.right)) + self.findTilt(root.left) + self.findTilt(root.right)
        return 0
      
    def sumHelper(self,root):
        if root:
            return root.val + self.sumHelper(root.left) + self.sumHelper(root.right)
        return 0
            