import math
class Solution:

#using fermat's theorem
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i = 2
        while i * i <= c:  
            count = 0
            if c % i == 0:
                while c % i == 0:
                    count += 1
                    c /= i
                if (i % 4 == 3 and count % 2 != 0):
                    return False
            i += 1
        return c % 4 != 3
    
#Naive Solution exceeds time limit for big numbers like 2147483645
#     def judgeSquareSum(self, c):
#         """
#         :type c: int
#         :rtype: bool
#         """
#         a = 0
#         while a*a <= c:  
#             if self.isPerfectSquare(c-a*a):
#                 return True
#             a += 1
#         return False
     
#     def isPerfectSquare(self, num):
#         """
#         :type num: int
#         :rtype: bool
#         """
#         if (num == 0 or num == 1) :
#             return True
    
#         start = 1
#         end = num 
#         ans = False
#         while start <= end:
#             mid = (start + end) // 2
#             if mid*mid == num:
#                 return True
#             if mid*mid < num:
#                 start = mid + 1
#                 ans = mid
#             else:
#                 end = mid - 1
#         return False