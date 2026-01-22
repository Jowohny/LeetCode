class Solution:
    def totalNQueens(self, n: int) -> int:

        #create a set for each type of space the queen piece occupies
        cSet = set()
        pdSet = set()
        ndSet = set()

        #use this as a counter for how many valid solutions this board size has
        res = 0

        #backtracking algorithm
        def backtrack(row):
            nonlocal res

            #if we have reached the final row, then add 1 to the total amount of valid solutions
            if row == n:
                res += 1

                #backtrack
                return

            #iterate through each column in the board
            for c in range(n):

                #only continue if the placement of the queen on the current cell doesn't interfere with the queens previously placed
                if c not in cSet and row+c not in pdSet and row-c not in ndSet:

                    #if the current queen is clear of all the others, then add the current queen's ocuppied spaces to their respective sets
                    cSet.add(c)
                    pdSet.add(row+c)
                    ndSet.add(row-c)

                    #recall the method to try out variations for the next row
                    backtrack(row+1)

                    #after finishing the latest path, remove the current queen's occupied spaces so we can test all the other possible combinations
                    cSet.remove(c)
                    pdSet.remove(row+c)
                    ndSet.remove(row-c)

        #initial call to the method
        backtrack(0)

        #return the total amount of viable solutions
        return res
