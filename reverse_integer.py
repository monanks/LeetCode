class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        m = 1 if x>0 else -1 
        s = str(abs(x))[::-1]
        n = m*int(s) 
        return n if abs(n) <= (pow(2,31)) else 0
        