class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if B in A:
                return 1
        tmp = A
        count = 1
        while len(tmp) <= len(B)*3:
            if B in tmp:
                return count
            tmp += A
            count += 1
        return -1