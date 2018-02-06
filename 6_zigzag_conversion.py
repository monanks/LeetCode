class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        ans = [""]*numRows
        dir = 1
        index = 0 
        for ch in s:
            ans[index] += ch
            if index == 0:
                dir = 1
            if index == numRows-1:
                dir = -1
            index += dir
        return "".join(ans)
                
                