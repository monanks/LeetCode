class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        else:
        #sol1
            return (num>0) and (num&(num-1)==0) and (num-1)%3==0
        #sol2
            b = bin(num)
            return b.count('1') == 1 and b[2:].count('0')%2 == 0