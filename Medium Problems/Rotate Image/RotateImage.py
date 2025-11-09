class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #set a dual pointer system, one for traversing through the rows and the another for traversing the columns
        #when setting the pointers for the rows, use the initial starting point of the columns pointers
        #we use those because it helps us rotate the matrix layer by layer
        #when rotating, the location of the point where the matrix's value goes to is the index of the left pointer in the perspective of the rows instead of the columns
        #we also go counter clockwise in terms of replace values in the matrix so we only use one temperary variable
        #after finishing the current layer, increment the left pointer and decrement the right pointer
        #since we are only changing in place, we dont return anything

        l,r = 0,len(matrix)-1

        while l < r:
            for i in range(r-l):
                t,b = l,r

                tl = matrix[t][l+i]
                matrix[t][l+i] = matrix[b-i][l]
                matrix[b-i][l] = matrix[b][r-i]
                matrix[b][r-i] = matrix[t+i][r]
                matrix[t+i][r] = tl

            l += 1
            r -= 1

        