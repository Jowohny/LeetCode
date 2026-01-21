class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        #create 3 types of set for each type of direction the queen can occupy
        cSet = set()
        pdSet = set()
        ndSet = set()

        #create an array to store all the possible solutions for the board
        res = []

        #fill an nxn array with dots to be arranged later
        board = [['.'] * n for _ in range(n)]

        #backtracking method
        def backtrack(row):

            #if the last row has been reached, then we have found a solution, turn the board into an array of string, 1 element for each row and add it to the result
            if row == n:
                final = [''.join(row) for row in board]
                res.append(final)
                return

            #explore every possible solution by trying each column in the current row
            for c in range(n):

                #only proceed if the placing the queen in the current column doesn't intercept with the others previously placed
                if c not in cSet and row+c not in pdSet and row-c not in ndSet:

                    #add the spaces that the queen in this space would occupy so later queens don't interfere with this one
                    cSet.add(c)
                    pdSet.add(row+c)
                    ndSet.add(row-c)

                    #change the current space on the board to a Q character to indicate the queen placement
                    board[row][c] = 'Q'

                    #call the method again to try other combinations
                    backtrack(row+1)

                    #after the backtracking for the current path is done, remove the previously added queen-occupied spaces so we can test other possible variations
                    cSet.remove(c)
                    pdSet.remove(row+c)
                    ndSet.remove(row-c)

                    #replace the Q with a . to start clean
                    board[row][c] = '.'

        #starting call to backtracking algorithm
        backtrack(0)

        #after the backtracking is done, return all the possible solutions found
        return res
