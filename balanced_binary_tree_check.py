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
        if not root:
            return True
        else:
            l,c= self.helper(root)
            return c
        
    def helper(self,node):
        if not node:
            return (0,True)
        else:
            l,c1 = self.helper(node.left)
            r,c2 = self.helper(node.right)
            #print(node.val)
            #print(l,c1)
            #print(r,c2)
            if c1 and c2 and abs(l-r)<2:
                return (max(l+1,r+1),True)
            else:
                return (-1,False)