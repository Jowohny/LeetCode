class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #define a set of directions so we can add all spaces horozontally and vertically from the current space
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        #keep a counter on how much time it takes along with how many fresh fruit there were
        time = 0
        total = 0

        #initialize deque
        q = deque()

        #explore every space in the grid, add all the rotton fruits the the deque and count all the fresh fruit
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    total += 1

        #loop until all rotten fruits are processed or the total amount of fresh fruit are 0
        while q and total > 0:

            #process all the current rotton fruit in the deque
            for _ in range(len(q)):

                #unpack the row and column from the most recent rotten fruit
                r,c = q.popleft()

                #check all neighbors from the current space
                for dr,dc in directions:

                    #check the surrounding fruits and make them rotten if they are within bounds and take away 1 from the total amount of fresh fruits left and add the newly rotten gruit to the deque
                    if 0 <= r+dr < len(grid) and 0 <= c+dc < len(grid[0]) and grid[r+dr][c+dc] == 1:
                        grid[r+dr][c+dc] = 2
                        total -= 1
                        q.append((r+dr, c+dc))

            #add 1 the total amount of time as each run through represents 1 round of rottenification
            time += 1

        #return the total amount of time to rot all the oranges unless there are still more fruit remaining, then return -1
        return time if total == 0 else -1
