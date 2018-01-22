class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans, count = 0, 0
        for i in xrange(len(nums)):
            if i == 0 or nums[i-1] < nums[i]:
                count += 1
                ans = max(ans, count)
            else:
                count = 1
        return ans