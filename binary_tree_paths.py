# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ans = []
        if root:
            self.treepath(root,str(root.val),ans)
        return ans
            
    def treepath(self,node,path,ans):
        if not node.left and not node.right:
            ans.append(path)
        if node.left:
            self.treepath(node.left,path+"->"+str(node.left.val),ans)
        if node.right:
            self.treepath(node.right,path+"->"+str(node.right.val),ans)