# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            l = self.minDepth(root.left)
            r = self.minDepth(root.right)
            #print(l,r,root.val)
            if l == 0:
                return r+1
            if r == 0:
                return l+1
            return min(l,r)+1
        