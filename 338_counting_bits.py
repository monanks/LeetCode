class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        ans = [0]
        offset = 1
        for i in range(1,num+1):
            if offset*2 == i:
                offset *= 2
            print(i-offset)
            ans.append(ans[i-offset] + 1)
        return ans