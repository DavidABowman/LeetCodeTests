#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
#Determine if the input string is valid

class Solution(object):
    def isValid(self, s):
        stack = [] # create an empty stack to store opening brackets
        for c in s: # loop through each character in the string
            if c in '([{': # if the character is an opening bracket
                stack.append(c) # push it onto the stack
            else: # if the character is a closing bracket
                if not stack or \
                    (c == ')' and stack[-1] != '(') or \
                    (c == '}' and stack[-1] != '{') or \
                    (c == ']' and stack[-1] != '['):
                    return False # the string is not valid, so return false
                stack.pop() # otherwise, pop the opening bracket from the stack
        return not stack # if the stack is empty, all opening brackets have been matched with their corresponding closing brackets,
                         # so the string is valid, otherwise, there are unmatched opening brackets, so return false



'''
Do Cut Me Slack
Today I moved back into Uni, meaning I didn't get much time to code 
Plus, I had to redownload GitHub, VSC, Python, etc. on Laptop
Anyways, this is all I had (Was Learning About Stacks):

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stack.append(s)
        stack.pop(s)

'''