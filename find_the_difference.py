class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return chr(reduce(lambda x,y : x^y, map(ord,s+t)))
#         sol using directory with extra space
#         count = {}
#         count[t[-1]] = 1
#         for i in range(len(s)):
#             if s[i] in count:
#                 count[s[i]] -= 1
#             else:
#                 count[s[i]] = -1
#             if t[i] in count:
#                 count[t[i]] += 1
#             else:
#                 count[t[i]] = 1
        
#         for i in count:
#             if count[i] == 1:
#                 return i