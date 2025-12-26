from collections import defaultdict

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        #total amount of stones before removal
        removableStones = len(stones)

        #dictionaries to store all connected stones through each unique row and column
        stoneRow = defaultdict(list)
        stoneCol = defaultdict(list)

        #populate row and column connections
        for i, (r, c) in enumerate(stones):
            stoneRow[r].append(i)
            stoneCol[c].append(i)

        #use a set to make indexes we've visited so we don't process the same one again
        visited = set()

        #technically doable without another method, but its here to make it more readable
        def dfs(i):
            nonlocal removableStones

            #every time we have to call this method, it's another set of stones that can't interact or remove each other due to being too unique
            removableStones -= 1

            #initially add index given through the method parameters to the stack to process
            stack = [i]

            #loop until the stack is empty
            while stack:

                #pop the stack to get the latest index
                sI = stack.pop()

                #unpack the current row and col given by the index of the stones list
                r,c = stones[sI]

                #process all connected pieces
                #only add connect indexed rows and columns if they weren't already visited
                #add those indexes to the visited set while we at it
                for row in stoneRow[r]:
                    if row not in visited:
                        stack.append(row)
                        visited.add(row)

                for col in stoneCol[c]:
                    if col not in visited:
                        stack.append(col)
                        visited.add(col)


        #go through all the indexes to process the outcome
        #only call the method if the index hasn't already been processed
        for i in range(len(stones)):
            if i not in visited:
                visited.add(i)
                dfs(i)

        #symbolizes the total amount of stones take away the amount of different uninteracted groups, which those amount of groups would be the amount of stones we wouldn't be able to remove        
        return removableStones