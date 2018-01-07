class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        ln = len(A)
        ans = [-1]*ln
        mark = [False]*ln
        print(ans,mark)
        for i in range(ln):
            a = A[i]
            for j in range(ln):
                if (B[j] == a) and (not mark[j]) and ans[i]==-1:
                    ans[i] = j
                    mark[j] = True
        return ans