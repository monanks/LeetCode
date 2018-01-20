class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return -1
        count = {}
        for ch in s:
            try:
                count[ch] += 1
            except KeyError:
                count[ch] = 1
        
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        return -1