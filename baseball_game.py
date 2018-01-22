class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        last, second_last, score = 0, 0, 0
        points = []
        for op in ops:
            if op == '+':
                points.append(points[-1] + points[-2])
                score += points[-1]
            elif op == 'D':
                points.append(points[-1] * 2)
                score += points[-1]
            elif op == 'C':
                score -= points.pop()
            else:
                points.append(int(op))
                score += points[-1]  
        return score
        