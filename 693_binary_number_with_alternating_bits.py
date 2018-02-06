class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        else:
            prev = n%2
            n = n/2
            while n:
                if n % 2 != prev:
                    prev = n % 2
                    n = n / 2
                else:
                    return False
            return True
        