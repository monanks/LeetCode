class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        number of coins (n) used to form k stairs are (k)*(k+1)/2 
        so n = sqrt(2 * n + .25) - .5
        """
        return int(math.sqrt(2 * n + .25) - .5)