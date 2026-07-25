class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #the number of ways to reach a cell is the ways from the cell above plus the ways from the cell to the left
        #an obstacle cell can never be reached, so set its number of paths to 0
        #reuse a single row as a rolling dp table, each value holds the paths to reach that column
        #seed the starting column with 1 path as long as the start cell isnt an obstacle
        #sweep row by row updating each column, the last value in the row is the answer

        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0

        dp = [0] * len(obstacleGrid[0])

        #one way to be standing on the starting cell
        dp[0] = 1

        for row in obstacleGrid:
            for c in range(len(row)):

                #an obstacle cant be reached, so no paths pass through it
                if row[c] == 1:
                    dp[c] = 0

                #add the paths coming from the left, dp[c] already holds the paths from above
                elif c > 0:
                    dp[c] += dp[c-1]

        return dp[-1]
