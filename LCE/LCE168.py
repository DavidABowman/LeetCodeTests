#Given an integer columnNumber,
#return its corresponding column title as it appears in an Excel sheet.

#Recursive Solution
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if not columnNumber:
            return ""
        columnNumber, remainder = divmod(columnNumber -1, 26)
        return self.convertToTitle(columnNumber) + chr(65 + remainder)



'''
#Iterative Approach
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber:
            columnNumber, remainder = divmod(columnNumber - 1, 26) # divmod = model operation, gets remainder when dividing by 26. 
            result.append(chr(65 + remainder))
        return ''.join(reversed(result))
        

        #Hashmap A-Z as 1 - 26
        #Divide int i by 26. 
        #Diviser corresponds to Letter 1. 
        #Modulus corresponds to Letter 2?
        #If Diviser > 26, Divide Again to Get Diviser 2 and Modulus
        '''