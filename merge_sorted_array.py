class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        j = m - 1
        for item in nums2:
            k = j
            while nums1[k] > item and k > -1:
                #print(k+1,k)
                nums1[k+1] = nums1[k]
                k -= 1
            j += 1
            nums1[k+1] = item
            #print(nums1)
        