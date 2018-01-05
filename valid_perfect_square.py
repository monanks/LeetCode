class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if (num == 0 or num == 1) :
            return True
    
        start = 1
        end = num 
        ans = False
        while start <= end:
            mid = (start + end) // 2
            if mid*mid == num:
                return True
            if mid*mid < num:
                start = mid + 1
                ans = mid
            else:
                end = mid - 1
        return False
        