class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<4:
            return n
        else:
            n1 = 3
            n2 = 2
            nn = 0
            for i in range(4,n+1):
                nn = n1 + n2
                n2 = n1
                n1 = nn
            return nn