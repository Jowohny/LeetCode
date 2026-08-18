class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        #we start at the given cell and spiral outward, only writing down the cells that actually sit inside the grid
        #the spiral walks east, south, west, north over and over, and the walk drifts outside the grid a lot
        #the trick is the step length grows as we go, we take 1 step, 1 step, 2 steps, 2 steps, 3 steps, 3 steps and so on
        #every two direction changes the step length bumps up by one, which is what makes the path spiral out
        #keep collecting cells until we have every cell in the grid, then were done

        #directions we cycle through in order, east then south then west then north
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        #the starting cell is always in the grid, so record it right away
        res = [[rStart, cStart]]

        #current position and how many total cells we still need to find
        r, c = rStart, cStart
        total = rows * cols

        #how many steps to take in the current direction, and which direction were facing
        steps = 1
        d = 0

        while len(res) < total:

            #the step length holds for two directions before it grows, so run the pair here
            for _ in range(2):
                dr, dc = directions[d % 4]

                #walk the current number of steps in this direction
                for _ in range(steps):
                    r += dr
                    c += dc

                    #only record the cell if it actually lands inside the grid
                    if 0 <= r < rows and 0 <= c < cols:
                        res.append([r, c])

                #turn to the next direction in the cycle
                d += 1

            #after every two directions the spiral reaches farther out, so take one more step next time
            steps += 1

        return res
