# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        start = 1
        end = n
        while True:
            mid = (start+end)//2
            a = isBadVersion(mid)
            b = isBadVersion(mid+1)
            first = (a != b)
            if first:
                return mid+1
            elif a and b:
                end = mid-1
            else:
                start = mid+1