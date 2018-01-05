class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
#binary search solution
        if (x == 0 or x == 1) :
            return x
    
        start = 1
        end = x   
        while start <= end:
            mid = (start + end) // 2
            if mid*mid == x:
                return mid
            if mid*mid < x:
                start = mid + 1
                ans = mid
            else:
                end = mid - 1
        return ans
        
        
# naive solution
#         if x == 0 or x == 1:
#             return x
#         else:
#             i = 1
#             sq = 1
#             while sq < x:
#                 i += 1
#                 sq  = i*i
#             if sq == x:
#                     return i
#             return i-1