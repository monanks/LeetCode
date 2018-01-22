class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        big = 0
        for i in range(len(nums)):
            if nums[big] < nums[i]:
                big = i
        small = set(nums)
        small.remove(nums[big])
        
        for i in small:
            if i*2 > nums[big]:
                return -1
        return big
            