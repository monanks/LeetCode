# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root == None:
            return []
        ans = self.doTraverse(root,[],0)
        res= []
        for i in ans:
            res.append(sum(i)/len(i))
        return res
    
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