class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if len(nums)==0:
        #     return 0
        # ans = 1
        # l = len(nums)
        # for i in range(l-1):
        #     if nums[i] != nums[i+1]:
        #         ans += 1
        # return ans
# second solution
        i = 0
        while i+1 < len(nums):
            t = nums[i]
            p = nums[i+1]
            if t == p:
                del nums[i+1]
            else:
                i += 1
        return len(nums)
        
# Naive Solution
        # i = 0        
        # while i < len(nums):
        #     t = nums[i]
        #     while True:
        #         #print(i,t)
        #         try:
        #             nums.remove(t)
        #         except:
        #             nums.insert(i,t)
        #             break
        #     i += 1
        #     #print(i,nums)
        # return len(nums)
                