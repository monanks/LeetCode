class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if str == "":
            return 0
        if str[0] == '-':
            res = -1*self.helper(str[1:])
        elif str[0] == '+':
            res = self.helper(str[1:])
        else:
            res = self.helper(str)
        if res > 2147483647:
            res = 2147483647
        elif res < -2147483648:
            res = -2147483648 
        return res
        
    def helper(self,s):
        if str == "":
            return 0
        res = 0
        for i in range(len(s)):
            if s[i] >= '0' and s[i] <= '9':
                res = res*10 + (ord(s[i]) - ord('0'))
            else:
                return res
        return res