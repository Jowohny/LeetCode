class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        #define the horizontal and vertical movement in respect to the grid
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        #use a set to store rows and columns within the grid so we don't revisit them
        visited = set()

        #use a min heap, storing with the effect as the key, alongside the row and the column to know where we are in the grid
        heap = [(0, 0, 0)]

        #loop until there are no more items in the heap or until we have reach the bottom right corner in the grid
        while heap:

            #pop off the item with the least amount of effort and unpack it
            effort,r,c = heapq.heappop(heap)

            #if we already have processed this row column pair in the visited set, skip it entirely
            if (r,c) not in visited:

                #add the current row and column combination into the visited sat
                visited.add((r,c))

                #if we have reached the bottom right cell, then return the least effort
                if r == len(heights)-1 and c == len(heights[0])-1:
                    return effort

                #attempt to travel in every direction
                for dr,dc in directions:

                    #check if the current direction is within bounds or hasn't been visited yet
                    if 0 <= r+dr < len(heights) and 0 <= c+dc < len(heights[0]) and (r+dr,c+dc) not in visited:

                        #if all conditions work, then use the absolute value of the current cell height subtracted by the height of the next cell as measure of value for the next iteration
                        #update the row and column as well
                        heapq.heappush(heap, (max(effort,abs(heights[r][c] - heights[r+dr][c+dc])), r+dr, c+dc))
                