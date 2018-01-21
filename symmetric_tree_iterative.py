# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            if root.left and root.right:
                lq = [root.left]
                rq = [root.right]
                while lq:
                    print(lq,rq)
                    lp = lq.pop()
                    rp = rq.pop()
                    if lp.val != rp.val:
                        return False
                    else:
                        if (not lp.left and rp.right) or (lp.left and not rp.right) or (not lp.right and rp.left) or (lp.right and not rp.left):
                            return False
                        if lp.left and rp.right:
                            lq.insert(0,lp.left)
                            rq.insert(0,rp.right)
                        if lp.right and rp.left:
                            lq.insert(0,lp.right)
                            rq.insert(0,rp.left)
            elif not root.left and not root.right:
                pass
            else:
                return False
        return True

#https://leetcode.com/articles/symmetric-tree/