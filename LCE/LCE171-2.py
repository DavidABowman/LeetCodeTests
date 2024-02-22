#Given a string columnTitle that represents the column title as appears in an Excel sheet,
#return its corresponding column number.

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            #Convert Character to corresponding number starting from 1
            num = ord(char) - ord('A') + 1
            #Multiply result by 26 and add the number
            result = result * 26 + num
        return result
'''
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
            ans, pos = 0, 0
            for letter in reversed(columnTitle):
                digit = ord(letter)-64
                ans += digit * 26**pos
                pos += 1
            return ans

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if not columnNumber:
            return ""
        columnNumber, remainder = divmod(columnNumber -1, 26)
        return self.convertToTitle(columnNumber) + chr(65 + remainder)
'''