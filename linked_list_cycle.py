# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fastrunner = head
        slowrunner = head
        while slowrunner and fastrunner and fastrunner.next:
            fastrunner = fastrunner.next.next
            slowrunner = slowrunner.next
            if fastrunner == slowrunner:
                return True
        return False
        