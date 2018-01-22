class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        l = len(letters)
        i = 0
        for i in range(l):
            if letters[i] > target:
                return letters[i]
        return letters[0]