#Given a specific rectangular web page’s area,  design a rectangular web page

#The area of the rectangular web page you designed must equal to the given target area.
#The width W should not be larger than the length L, which means L >= W.
#The difference between length L and width W should be as small as possible.
#Return an array [L, W] where L and W are the length and width of the web page 

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        width = int(area ** 0.5)
        while area % width != 0:
            width -= 1
        length = area // width
        return [length, width]