#Given a string s, reverse only all the vowels in the string and return it.

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left = 0
        right = len(s) - 1
        m = 'aeiouAEIOU'
        while left < right:
            if s[left] in m and s[right] in m:
                
                s[left], s[right] = s[right], s[left]
                
                left += 1; right -= 1
            
            elif s[left] not in m:
                left += 1
            
            elif s[right] not in m:
                right -= 1
            
        return ''.join(s)
        #Would be better if vowels were a set rather than a string
'''
#Just Hash this following code with vowels
class Solution:
    def reverseString(self, s: List[str]) -> None:
        hash = {a = a}
        s{::-1} = s
'''