class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #define a list of directions to navigate within the array
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        #use a heap to to choose the lowest time at each point within the array to explore around
        heap = [(grid[0][0],0,0)]

        #use a set to prevent processing the same cell multiple times
        visited = set()

        #loop until all cells are processed
        while heap:

            #pop the item with the lowest time in the current heap and unpack it
            time, row, col = heapq.heappop(heap)

            #if we reach the bottom right corner of the grid, we are done
            if row == len(grid)-1 and col == len(grid)-1:
                return time

            #add the current grid cell to the visited set to avoid processing this cell again later
            visited.add((row,col))

            #use directions list to explore around the current cell
            for dr,dc in directions:

                #if the cell is within the bounds of the array and it hasnt been visited yet, compare the greatest cell value we've encountered so far to the next cell value, then push it back onto the heap with next next cell's row and column
                #add the next cell's row and column pair to the visited set
                if 0 <= dr+row < len(grid) and 0 <= dc+col < len(grid) and (dr+row,dc+col) not in visited:
                    visited.add((dr+row,dc+col))
                    heapq.heappush(heap, (max(time,grid[dr+row][dc+col]), dr+row, dc+col))