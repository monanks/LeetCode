class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_set = set()
        
        for i in nums:
            if i in new_set:
                return i
            else:
                new_set.add(i)