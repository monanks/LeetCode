class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        count = 0
        for i in range(1,N+1):
            i *= 1.0
            if (N/i)-(i/2) < 0:
                break
            if (N/i)%1 == 0 and i%2 == 1:
                count += 1
            elif (N/i)%1 == 0.5 and i%2 == 0:
                count += 1
            
        return count
        