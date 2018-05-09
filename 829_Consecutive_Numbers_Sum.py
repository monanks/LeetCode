class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        #method 2
        
        count = 1
        t = math.sqrt(2*N)
        i = 2
        while i < t:
            if ( N - ( i * (i -1) / 2 )) % i == 0:
                count += 1
            i += 1

        return count
        
#         #method 1
#         count = 0
#         i = 1.0
#         while(1):
#             if (N/i)-(i/2) < 0:
#                 break
#             if (N/i)%1 == 0 and i%2 == 1:
#                 count += 1
#             elif (N/i)%1 == 0.5 and i%2 == 0:
#                 count += 1
#             i += 1
            
#         return count
        