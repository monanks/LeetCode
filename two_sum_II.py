import itertools
class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        look = {}
        for i,num in enumerate(numbers):
            if target-numbers[i] in look:
                return [look[target - num]+1,i+1]
            look[num] = i