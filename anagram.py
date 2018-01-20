class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sc = set(s+t)
        
        for c in sc:
            if s.count(c) != t.count(c):
                return False
        return True