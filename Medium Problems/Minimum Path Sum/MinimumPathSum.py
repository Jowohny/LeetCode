class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #we can only move right or down, so the cheapest way to reach a cell comes from either the cell above or the cell to the left
        #pick the smaller of those two and add the current cell's value on top
        #reuse a single row as a rolling dp table, each value holds the cheapest cost to reach that column
        #seed the first row by just adding across, since theres only one way to walk along it
        #for every row after, fold in the cost from above and from the left, the last value is the answer

        cols = len(grid[0])

        #dp holds the cheapest cost to reach each column, start it as the very first row
        dp = [0] * cols
        dp[0] = grid[0][0]

        #the first row can only be reached by walking right, so just keep adding across
        for c in range(1, cols):
            dp[c] = dp[c - 1] + grid[0][c]

        for r in range(1, len(grid)):

            #the first column can only be reached from the cell above it
            dp[0] += grid[r][0]

            for c in range(1, cols):

                #cheapest of coming from above (dp[c]) or from the left (dp[c-1]), plus this cell
                dp[c] = grid[r][c] + min(dp[c], dp[c - 1])

        return dp[-1]
