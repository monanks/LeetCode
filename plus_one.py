class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = int("".join(map(str,digits)))+1
        return list(map(int,list(str(n))))