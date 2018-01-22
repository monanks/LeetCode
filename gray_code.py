class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        l = ['0','1']
        j = 1
        while j < n:
            ln = len(l)
            for i in range(ln):
                l.insert(ln,"1"+l[i])
                l[i] = "0"+l[i]
            j += 1        
        return [int(x,2) for x in l]
        