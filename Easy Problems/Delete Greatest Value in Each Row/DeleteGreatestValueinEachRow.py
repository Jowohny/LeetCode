class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        #keep the sum of all minimum or maximum values popped from each step
        res = 0

        #heapify all rows within the grid to prep for popping later
        for r in grid:
            heapq.heapify(r)

        #run for the length of the row
        for _ in range(len(grid[0])):

            #put all popped row vales into the the list
            cr = []

            #pop the greatest or smallest value within the row (either or it doesn't really matter)
            for r in grid:
                cr.append(heapq.heappop(r))

            #find the max value within all the popped values and add it to the result
            res += max(cr)

        #return the sum of all the minimum or maximum values popped from the array
        return res