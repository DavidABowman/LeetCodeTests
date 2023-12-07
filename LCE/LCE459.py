#Given a string s, check if it can be constructed by taking a substring of it 
#and appending multiple copies of the substring together.

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
      length = len(s)
      for i in range(1, length // 2 + 1):
          if length % i == 0:
              substring = s[:i]
              if substring * (length // i) == s:
                  return True
      return False