#I pick a number from 1 to n. You have to guess which number I picked.
#Every time you guess wrong, I will tell you whether the number I picked is higher or lower.

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        return bisect_left(range(n), 0, key=lambda num: -guess(num))
'''
class Solution:
    def guessNumber(self, n: int) -> int:
        lowerBound, upperBound = 1, n
        myGuess = (lowerBound+upperBound) >> 1

        while (res := guess(myGuess)) != 0: 
            #NarwhalOperator assings val of func. to var. 'res', to then compare res w/ 0
            if res == 1:
                lowerBound = myGuess+1
            else:
                upperBound = myGuess-1
            myGuess = (lowerBound+upperBound) >> 1
        return myGuess
'''