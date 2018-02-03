class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total_sum = (len(nums)*(len(nums)+1))//2
        missing_sum = sum(set(nums))
        duplicate_sum = sum(nums)
        missing = total_sum - missing_sum
        duplicate = duplicate_sum - missing_sum
        
        return [duplicate,missing]
        
#         slower approach
#         count = [0]*len(nums)
#         for i in nums:
#             count[i-1] += 1
        
#         for i in range(len(nums)):
#             if count[i]==2:
#                 one = i+1
#             if count[i]==0:
#                 two = i+1
        
#         return [one,two]
        