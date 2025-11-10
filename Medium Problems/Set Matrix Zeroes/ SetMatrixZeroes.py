class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        #create 2 arrays the length of the sides of the matrix and populate them with 1
        #go through the whole matrix and assign 0 values to the respective index in the respective arrays
        #after running through the matrix the first time, the 2 arrays should be fitted to know which rows and which columns need to be made 0
        #run through the matrix a second time check the arrays for that 0 value, if either one of them come backs as needed to be 0, then the value at the point in the matrix will be set to 0

        rows,cols = len(matrix),len(matrix[0])
        rowZero,colZero = [1]*rows,[1]*cols
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    rowZero[r] = 0
                    colZero[c] = 0
        
        for r in range(rows):
            for c in range(cols):
                if not rowZero[r] or not colZero[c]:
                    matrix[r][c] = 0
            
        