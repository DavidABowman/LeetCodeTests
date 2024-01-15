#Given two strings needle and haystack, return the index of the first occurrence of 
#needle in haystack, or -1 if needle is not part of haystack.

#Round 2
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0 #Empty needle always found at index 0
        h_len, n_len = len(haystack), len(needle)

        for i in range(h_len - n_len +1):
            if haystack[i:i+n_len] == needle:
                return i
        return -1 #Needle not found
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        location = 0 
        for i in range(len(haystack)):
            if location[i] in needle:
                location += 1
            else:
                return -1
'''
