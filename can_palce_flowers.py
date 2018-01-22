class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        
        i = 1
        flowerbed.insert(0,0)
        flowerbed.append(0)
        while i+1 < len(flowerbed):
            if not flowerbed[i-1] and not flowerbed[i] and not flowerbed[i+1]:
                flowerbed[i] = 1
                n -= 1
                i += 2
            else:
                i += 1
            
        if n <= 0:
            return True
        return False