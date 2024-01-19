#Given two binary strings a and b, return their sum as a binary string

#2nd try
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0

        a = a.zfill(max(len(a), len(b)))
        b = b.zfill(max(len(a), len(b)))

        for i in range(len(a) -1, -1, -1):
            bit_sum = int(a[i]) + int(b[i]) + carry
            result.append(str(bit_sum % 2))
            carry = bit_sum // 2

        if carry:
            result.append(str(carry))
        return ''.join(result[::-1])
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a,2)+int(b,2)))[2:]

#I messed up, I thought I was just making a regular calculator
#So I was getting confused when converting into integers didn't work lmao
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = int(a%2) + int(b%2)
        print(result%2)
'''