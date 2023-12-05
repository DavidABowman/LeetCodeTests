#Given a string s, return the number of segments in the string.

class Solution:
    def countSegments(self, s: str) -> int:
        segments = s.split()
        return len(segments)
'''
class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        inside_segment = False

        for chr in s:
            if chr != ' ' and not inside_segment:
                count += 1
                inside_segment = True
            elif chr == ' ' and inside_segment:
                inside_segment == False
        return count'
        '''