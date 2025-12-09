class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #create a row and column count for convenient use later
        rows, cols = len(board), len(board[0])

        #use dfs to search in every direction from the current at each step
        def search(r, c, i):
            #if the length of the index given by the parameter is up to the length of the word, that means we have successfully found the word
            if i == len(word):
                return True

            #check whether the current row and column is in bounds
            #also check if the cell was already visited or if the current index in the word doesn't match the current letter on the board
            #in those cause, end the current branch
            if (r < 0 or c < 0 or r >= rows or c >= cols or 
                board[r][c] != word[i] or board[r][c] == -1):
                return False

            #store a temporary value for restoring the board later
            temp = board[r][c]

            #mark the current space as visited to avoid going backwards
            board[r][c] = -1

            #branch out from the current space on the board in all directions
            #chain them together in the case that at least 1 one could be the path to the solution
            found = (
                search(r+1, c, i+1) or
                search(r-1, c, i+1) or
                search(r, c+1, i+1) or
                search(r, c-1, i+1)
            )

            #restore value for other paths
            board[r][c] = temp

            #if at least one path found something, this returns 
            return found

        #start from every possible cell
        for r in range(rows):
            for c in range(cols):
                if search(r, c, 0):
                    return True

        #if the search from no where in the grid yields results, our word is not in the grid 
        return False
