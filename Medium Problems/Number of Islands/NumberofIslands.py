class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #keep a tracker to know the total amount of islands throughout the search
        res = 0

        #explore every direction from the given row and column
        def dfs(r,c):

            #if the current space is out of bounds or is water, stop the exploration in this direction
            if r >= len(grid) or r < 0 or c >= len(grid[0]) or c < 0 or grid[r][c] == '0':
                return

            #set the current space to 0 to represent it as ocean so we don't revisit it again later
            grid[r][c] = '0'

            #define the directions for variations
            directions = [(1,0),(-1,0),(0,1),(0,-1)]

            #explore each direction horozontally and vertically defined by the directions array
            for dr,dc in directions:
                dfs(r+dr, c+dc)

        #use every space in the grid as a potential start for a new island search
        for r in range(len(grid)):
            for c in range(len(grid[0])):

                #if the current space is a piece of land, add one to the total amount of islands and explore the rest
                if grid[r][c] == '1':
                    res += 1
                    dfs(r,c)

        #return the total amount of found islands in the array
        return res