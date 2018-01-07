class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = [1,1]
        if rowIndex < 2:
            return ans[:rowIndex+1]
        else:
            for i in range(2,rowIndex+1):
                temp = []
                temp.append(1)
                for j in range(i-1):
                    temp.append(ans[j]+ans[j+1])
                temp.append(1)
                ans = temp
            return ans 