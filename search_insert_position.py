class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        for i,num in enumerate(nums):
            if target == num or target < num:
                return i
        return i+1
            
        