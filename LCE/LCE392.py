#Given two strings, s and t, the challenge is to determine if s is a subsequence of t.

#TwoPointers, one for each string
#We created while loop during each iteration which checks if current chr is s = t
#We increment pointer in t, where match is found or not. If not, =+ 1
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        s_pointer = 0
        t_pointer = 0
        while t_pointer < len(t):
            if t[t_pointer] == s[s_pointer]:
                s_pointer += 1
                if s_pointer == len(s):
                    return True
            t_pointer += 1
        return False