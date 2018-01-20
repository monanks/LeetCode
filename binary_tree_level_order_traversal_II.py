# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        return self.doTraverse(root,[],0)
    
    def doTraverse(self,root,ans,level):
        
        try:
            ans[level-1].append(root.val)
        except IndexError:
            ans.insert(0,[root.val])
        if root.left:
            ans = self.doTraverse(root.left,ans,level-1)
        if root.right:
            ans = self.doTraverse(root.right,ans,level-1) 
        return ans