#Determine the perimeter of the island, given row x col grid representing a map 
#where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
'''
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    perimeter += 4
                
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2

        return perimeter  
'''
class Solution:
		def islandPerimeter(self, grid: List[List[int]]) -> int:
			isLands = 0
			nghbrs = 0
			grd_len = len(grid)
			grd0_len = len(grid[0])
			for i in range(grd_len):
				for j in range(grd0_len):
					if grid[i][j] == 1:
						isLands += 1
						if i < grd_len-1 and grid[i+1][j] == 1:
							nghbrs += 1  # Counting next Down Neighbour...
						if j < grd0_len-1 and grid[i][j+1] == 1:
							nghbrs += 1  # Counting next Right Neighbour...
			return 4*isLands - 2*nghbrs                 