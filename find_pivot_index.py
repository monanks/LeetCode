class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        s = 0
        i = 0
        for i in range(len(nums)):
            if s == total-s-nums[i]:
                return i
            print(s,total)
            s += nums[i]
        return -1