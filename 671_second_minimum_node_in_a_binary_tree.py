# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        s = set()
        self.collect(root,s)
        if len(s) < 2:
            return -1
        else:
            s.remove(min(s))
            return min(s)
        
    def collect(self,root,s):
        if not root:
            return
        else:
            s.add(root.val)
            self.collect(root.left,s)
            self.collect(root.right,s)