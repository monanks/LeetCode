class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        low = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] - low > profit:
                profit = prices[i] - low
            if prices[i] < low:
                low = prices[i]
        return profit

# s = Solution()
# print(s.maxProfit([7, 6, 4, 3, 1]))