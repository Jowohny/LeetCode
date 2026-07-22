class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        #treat each row as the base of a histogram built from the rows above it
        #for every column, if the cell is a '1' add to its running height, if its a '0' reset that height back to 0
        #once we have the heights for a row, run largest rectangle in histogram on it
        #use a stack to keep track of bars and their start positions
        #if the current bar is shorter than the one on top of the stack, pop and calculate the area for each bar
        #the largest area found across every row is the answer

        if not matrix:
            return 0

        maxArea = 0
        heights = [0] * len(matrix[0])

        for row in matrix:

            #build up the histogram heights for this row
            for i, val in enumerate(row):
                heights[i] = heights[i] + 1 if val == '1' else 0

            #largest rectangle in histogram on the current heights
            stack = []
            for i, h in enumerate(heights):
                sI = i
                while stack and stack[-1][1] > h:
                    index, height = stack.pop()
                    sI = index
                    maxArea = max(maxArea, height * (i - index))
                stack.append((sI, h))

            #clear out any bars still left in the stack, extending them to the end of the row
            for i, h in stack:
                maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea
