class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #keep track of the largest found island throughout the cycle
        largest = 0

        #explore in every direction from the current space
        def dfs(r,c):

            #if the current row or column isn't or if the current space isnt land, return 0 to represent that the current path doesn't yeild anything promising
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
                return 0

            #mark this place as 0 to represent it as ocean so we dont visit it later
            grid[r][c] = 0

            #add 1 to show that this was a valid space for land and explore in all 4 directions
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)

        #use every space in the grid as a starting point to find new islands
        for r in range(len(grid)):
            for c in range(len(grid[0])):

                #if the current space represents land then compare the largest island found through the current space with the largest found
                if grid[r][c] == 1:
                    largest = max(largest, dfs(r,c))
            
        #after exploring all grid spaces, return the largest island found
        return largest