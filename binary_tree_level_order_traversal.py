# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        return self.doTraverse(root,[],0)
        
    def doTraverse(self,root,ans,level):
        
        try:
            ans[level].append(root.val)
        except IndexError:
            ans.append([root.val])
        if root.left:
            ans = self.doTraverse(root.left,ans,level+1)
        if root.right:
            ans = self.doTraverse(root.right,ans,level+1) 
        return ans