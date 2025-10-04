class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #create new array variable
        #while we have something in the matrix, we loop until its empty
        #we start off every loop with popping the first row, the popping the last elements of the row going down,
        #then popping the last layer
        #everything we pop, we add to the array variable

        spiralarray = []

        while matrix:
            spiralarray += matrix.pop(0)

            if matrix and matrix[0]: 
                for row in matrix:
                    spiralarray.append(row.pop()) 
            if matrix:
                spiralarray += matrix.pop()[::-1] 
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    spiralarray.append(row.pop(0))

        return spiralarray