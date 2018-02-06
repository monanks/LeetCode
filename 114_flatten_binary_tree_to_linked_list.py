# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root == None:
            return
        else:
            if root.right == None and root.left == None:
                return
            elif root.right != None and root.left == None:
                self.flatten(root.right)
                return
            elif root.right == None and root.left != None:
                self.flatten(root.left)
                root.right = root.left
                root.left = None
                return
            else:
                self.flatten(root.left)
                self.flatten(root.right)
                node = root.left
                while node.right:
                    node = node.right
                node.right = root.right
                root.right = root.left
                root.left = None
                return
        