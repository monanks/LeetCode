class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = [[1],[1,1]]
        if numRows < 3:
            return ans[:numRows]
        else:
            for i in range(2,numRows):
                ans.append([1])
                for j in range(i-1):
                    ans[i].append(ans[i-1][j]+ans[i-1][j+1])
                ans[i].append(1)
            return ans       

s = Solution()
print(s.generate(10))