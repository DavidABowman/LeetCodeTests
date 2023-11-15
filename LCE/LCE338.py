#Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
#ans[i] is the number of 1's in the binary representation of i.



class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1) #Initialise Array of size n+1 with all 0s
        for i in range(1, n + 1): 
            #For each 1 to n, we calculate all no.s of 1 by summing 1s by right shifting all 1s to the right (or synonymous with dividng by 2)
            res[i] = res[i >> 1] + (i & 1) 
            #i shifting right (right shift operator) qual to dividing by 2) - if odd, it adds 1
        return res

'''
class Solution:
    def countBits(self, n: int) -> List[int]:
        return[sum(map(int, bin(i)[2:])) for i in range (n + 1)]
'''