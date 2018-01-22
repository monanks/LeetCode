class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans =[-1,-1]
        if len(nums)==0 or target < nums[0] or target > nums[-1] :
            return ans
        else:
            nums.insert(0,-1)
            nums.append(0)
            found = False
            for i in range(len(nums)-1):
                if not found and nums[i] != target and nums[i+1] == target:
                    found = True
                    ans[0] = i
                    break
            if not found:
                return ans
            for i in range(ans[0],len(nums)-1):
                if nums[i] == target and nums[i+1] != target:
                    found = True
                    ans[1] = i-1
                    break
            return ans
                