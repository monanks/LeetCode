# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root:
            temp = self.doTraverse(root,[],0)
            
                    
    
    def doTraverse(self,root,ans,level): 
        try:
            ans[level][-1].next = root
            ans[level].append(root)
        except IndexError:
            ans.append([root])
        if root.left:
            ans = self.doTraverse(root.left,ans,level+1)
        if root.right:
            ans = self.doTraverse(root.right,ans,level+1) 
        return ans
        