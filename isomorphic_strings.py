class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        x = set(t)
        change = {}
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                try:
                    if change[s[i]] != t[i] :
                        return False
                except KeyError:
                    if t[i] in x:
                        change[s[i]] = t[i]
                        x.remove(t[i])
                    else:
                        return False
            return True
        