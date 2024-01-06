#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_mapping = {')': '(', '}': '{', ']': '['}

        for chr in s:
            if chr in bracket_mapping.values():
                stack.append(chr)
            elif chr in bracket_mapping.keys():
                if not stack or stack.pop() != bracket_mapping[chr]:
                    return False
            else:
                return False

        return not stack