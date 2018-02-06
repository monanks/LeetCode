class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        b = bin(n)
        return int( b[2:][::-1] + "0"*(34-len(b)), 2)
s = Solution()
print(s.reverseBits(1))