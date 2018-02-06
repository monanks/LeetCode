# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        if root:
            self.doTraverse(root,ans,0)
        return ans

    def doTraverse(self,root,ans,level): 
        try:
            ans[level] = max(ans[level],root.val)
        except IndexError:
            ans.append(root.val)
        if root.left:
            self.doTraverse(root.left,ans,level+1)
        if root.right:
            self.doTraverse(root.right,ans,level+1) 