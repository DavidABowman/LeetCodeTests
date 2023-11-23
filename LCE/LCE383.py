#Given two strings ransomNote and magazine, 
#return true if ransomNote can be constructed by using the letters from magazine and false otherwise

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        st1, st2 = Counter(ransomNote), Counter(magazine)
        if st1 & st2 == st1:
            return True
        return False