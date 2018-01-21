# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ans = []
        if root:
            self.sumHelper(root,[root.val],ans,sum)
        return ans
    
    def sumHelper(self,node,path,ans,s):
        if not node.left and not node.right and s == sum(path):
            ans.append(path)
        if node.left:
            t = path[:]
            t.append(node.left.val)
            self.sumHelper(node.left,t,ans,s)
        if node.right:
            t = path[:]
            t.append(node.right.val)
            self.sumHelper(node.right,t,ans,s)


# Solution 2 Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        stack = [[root,root.val]]
        while stack:
            node, tot = stack.pop()
            if not node.left and not node.right and tot == target:
                return True
            if node.left:
                stack.append([node.left, node.left.val + tot])
            if node.right:
                stack.append([node.right, node.right.val + tot])
        return False