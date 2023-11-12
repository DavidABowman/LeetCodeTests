#Given n, the number of stones in the heap, 
#return true if you can win the game assuming both you and your friend play optimally, 
#otherwise return false.

'''
class Solution:
    def canWinNim(self, n:int) -> bool:
        return '1' in bin(n)[-2:]

class Solution:
    def canWinNim(self, n:int) -> bool:
        return n % 4 != 0
'''
#100% me :D
class Solution:
    def canWinNim(self, n: int) -> bool:
        if n%4 == 0:
            return False
        else:
            return True
'''
#Dynamic Programming
class Solution:
    def canWinNim(self, n: int) -> bool:        
        if n <= 3:
            return True
        new_size = n + 1
        memo = [False] * (new_size)
        
        for i in range(4): 
            memo[i] = True
        
        for i in range(4,new_size):
            for j in range(1,4):
                if memo[i] == True:
                    break
                if memo[i-j] == True:
                    memo[i] = False
                else:
                    memo[i] = True
        
        return memo[n]
'''