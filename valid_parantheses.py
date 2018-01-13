class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opening = set('({[')
        stack = []
        for br in s:
            if br in opening:
                stack.append(br)
            else:
                if len(stack) > 0:
                    if br == '}' and stack.pop() == '{':
                        pass
                    elif br == ']' and stack.pop() == '[':
                        pass
                    elif br == ')' and stack.pop() == '(':
                        pass
                    else:
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
        