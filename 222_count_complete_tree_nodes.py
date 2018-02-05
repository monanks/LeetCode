# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        height = 1
        left = root.left
        right = root.right
        while right:
            height += 1
            right = right.right
            left = left.left
        
        if not left:
            return 2**height -1
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1