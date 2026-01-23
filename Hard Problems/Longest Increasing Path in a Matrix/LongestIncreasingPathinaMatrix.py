class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        #use this to dynamically track the longest path as we check through the entire array
        res = 0

        #create a table of the same size as the matrix
        #each point displays the longest path found from that point forward
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        #depth first search method
        def dfs(r,c):

            #by default, visited cells are labeled with a number of at least 1, if its 0, then that cell hasn't been visited yet
            if dp[r][c] != 0:
                return dp[r][c]

            #directions array to give let the instruct how the dfs searches around its cell
            directions = [(0,1), (0,-1), (1,0), (-1,0)]

            #default longest path value set to 1
            best = 1

            #search every direction given by the directions array
            for dr, dc in directions:

                #only go in the given direction if the next cell is in bounds of the array and the next cell has a greater value than the current one
                if 0 <= r+dr < len(matrix) and 0 <= c+dc < len(matrix[0]) and matrix[r+dr][c+dc] > matrix[r][c]:

                    #dynamically update the longest length by adding 1 to each dfs call as we search a new cell every time the method is called
                    best = max(best, 1 + dfs(r+dr, c+dc))

            #update the dp array with the longest path found starting from this cell
            dp[r][c] = best

            #return the longest path found to dynamically update paths preceding this cell
            return best

        #start the search from each cell in the array
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):

                #update the final longest increasing path as we explore the array
                res = max(res, dfs(r,c))

        #return the final longest path found in the given matrix
        return res
            