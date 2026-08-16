class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        #we fill an n by n grid with 1 up to n squared while spiraling inward
        #keep four boundaries, top and bottom rows and left and right columns, that close in as we go
        #walk left across the top row, down the right column, back across the bottom row, then up the left column
        #after finishing each side, pull that boundary in one step so we dont fill the same cell twice
        #keep a running counter thats placed into each cell and bumped up by one every time

        #start with an empty n by n grid to drop the numbers into
        matrix = [[0] * n for _ in range(n)]

        #the four edges of the part of the grid we still need to fill
        top, bottom = 0, n - 1
        left, right = 0, n - 1

        #the next number to place, counts up to n squared
        num = 1

        while top <= bottom and left <= right:

            #walk left to right across the top row
            for c in range(left, right + 1):
                matrix[top][c] = num
                num += 1
            top += 1

            #walk top to bottom down the right column
            for r in range(top, bottom + 1):
                matrix[r][right] = num
                num += 1
            right -= 1

            #walk right to left across the bottom row
            for c in range(right, left - 1, -1):
                matrix[bottom][c] = num
                num += 1
            bottom -= 1

            #walk bottom to top up the left column
            for r in range(bottom, top - 1, -1):
                matrix[r][left] = num
                num += 1
            left += 1

        return matrix
