class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return False
        total = 1
        for i in range(2,int(math.sqrt(num))+1):
            if num%i == 0:
                a = num//i
                if i > a:
                    break
                total += (i + a)                
        if total == num or total-int(math.sqrt(num)) == num:
            return True
        return False

# class Solution2:
#     def checkPerfectNumber(self, num):
#         """
#         :type num: int
#         :rtype: bool
#         """
#         if num<=1: return False
#         s=int(num**0.5)
#         res=0
#         for i in range(2,s+1):
#             if num%i==0:
#                 if num/i!=i:
#                     res+=i+num/i
#                 else:
#                     res+i
#         return res+1==num

# s = Solution2()

# i = 2
# while True:
#     print(s.checkPerfectNumber(i*i),i*i)
#     i += 1