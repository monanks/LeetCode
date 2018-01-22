class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        last = 0
        while i < len(bits):
            if bits[i] == 0:
                i += 1
                last = 1
            elif bits[i] == 1:
                i += 2 
                last = 2
        return last == 1