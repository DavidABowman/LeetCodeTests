#Given an integer num, return a string representing its hexadecimal representation. 
#For negative integers, two’s complement method is used. 
#https://en.wikipedia.org/wiki/Two%27s_complement

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0: return '0'
        map = '0123456789abcedf'
        result = ''
#If negative (two's complement)
        if num < 0: num += 2 ** 32
        while num > 0:
            digit = num % 16
            num = (num - digit) // 16
            result += str(map[digit])
        return result[::-1]
'''
class Solution:
    def toHex(self, num: int) -> str:
        d = {10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        res = ""
        if num == 0:
            return "0"
        if num<0:
            num = (1<<32)+num
        while num>0:
            if num%16<10:
                res+=str(num%16)
            else:
                res+=str(d[num%16])
            num = num//16
        return res[::-1]
'''