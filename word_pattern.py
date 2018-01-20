class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        l = len(pattern)
        x = set()
        change = {}
        if l != len(words):
            return False
        else:
            for i in range(l):
                try:
                    if change[words[i]] != pattern[i] :
                        return False
                except KeyError:
                    if pattern[i] not in x:
                        change[words[i]] = pattern[i]
                        x.add(pattern[i])
                    else:
                        return False
            return True