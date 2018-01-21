# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        temp = self.doTraverse(root,[],0)
        
        return [l[-1] for l in temp]
    
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
        