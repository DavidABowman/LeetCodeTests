#Given two binary strings a and b, return their sum as a binary string

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a,2)+int(b,2)))[2:]

'''
#I messed up, I thought I was just making a regular calculator
#So I was getting confused when converting into integers didn't work lmao
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = int(a%2) + int(b%2)
        print(result%2)
'''