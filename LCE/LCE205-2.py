#Given two strings s and t, determine if they are isomorphic

class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False #If lengths aren't same, they can't be isomorphic
        s_to_t = {}
        t_to_s = {}#Mappings
        for i in range(len(s)):
            if s[i] in s_to_t:
                if s_to_t[s[i]] != t[i]: #Violation of Ismorphic Condition
                    return False
            else:
                s_to_t[s[i]] = t[i]
            if t[i] in t_to_s:
                if t_to_s[t[i]] != s[i]: #Violation
                    return False
            else:
                t_to_s[t[i]] = s[i]
        return True
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return [*map(s.index, s)] == [*map(t.index, t)]
        

class Solution(object):
    def isIsomorphic(self, s, t):
        map1 = []
        map2 = []
        for idx in s:
            map1.append(s.index(idx))
        for idx in t:
            map2.append(t.index(idx))
        if map1 == map2:
            return True
        return False
'''