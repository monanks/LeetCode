class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2:
            return True
        l = len(s)
        x = 0
        y = l-1
        s = s.lower()
        while x < y:
            while x < l and not s[x].isalnum():
                print(x,s[x])
                x += 1
            while y >= 0 and not s[y].isalnum():
                print(y,s[y])
                y -= 1
            if x <l and y >= 0 and s[x] != s[y]:
                print(x,y,s[x],s[y])
                return False
            x += 1
            y -= 1
        return True

#second solution using regular expression to remove non alphanumeris chars
import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new = re.sub(r'\W+',"",s)
        return new.lower() == new.lower()[::-1] 
        
s = Solution()

print(s.isPalindrome(".,"))