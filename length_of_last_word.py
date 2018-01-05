class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = 0
        s = s.strip()
        for i  in range(len(s)-1,-1,-1):
            if s[i] == " ":
                return index
            else:
                index += 1
        return index