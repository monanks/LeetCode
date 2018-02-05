class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        else:
            return 3**20 % n == 0
        
        # with use of loop
        # if n <= 0:
        #     return False
        # while n % 3 == 0:
        #     n /= 3
        # return n == 1