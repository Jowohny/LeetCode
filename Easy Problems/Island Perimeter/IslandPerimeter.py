class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #keep a counter for the total perimeter
        res = 0

        #iterate through all grid spaces
        for r in range(len(grid)):
            for c in range(len(grid[0])):

                #if the current grid represents land, add an initial 4 to the paremeter
                if grid[r][c]:
                    res += 4 

                    #if there is a another piece of land connect on the top or right next to it, take off 2 for each connected land to the current spot on the grid
                    if r > 0 and grid[r-1][c]:
                        res -= 2
                    if c > 0 and grid[r][c-1]:
                        res -= 2 

        #return the total perimeter
        return res
