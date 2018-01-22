class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans = []
        for i in range(left,right+1):
            if self.dividingNumbers(i):
                ans.append(i)
        return ans
        
    def dividingNumbers(self,num):
        l = list(map(int,str(num)))
        for i in l:
            if i == 0 or num%i != 0:
                return False
        return True