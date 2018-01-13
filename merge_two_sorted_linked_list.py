# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur1 = l1
        cur2 = l2
        l = ListNode(0)
        cur = l
        while cur1 and cur2:
            t = ListNode(0)
            cur.next = t
            if cur1.val >= cur2.val:
                t.val = cur2.val
                cur2 = cur2.next
            else:
                t.val = cur1.val
                cur1 = cur1.next
            cur = t 
        if cur1 != None:
            cur.next = cur1
        if cur2 != None:
            cur.next = cur2
        return l.next