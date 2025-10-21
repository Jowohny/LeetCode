class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #use a stack to keep track of bars and their start positions
        #go through each bar from left to right
        #if the current bar is shorter than the one on top of the stack, pop from the stack and calculate the area for each bar
        #push the current bar with the updated start index into the stack
        #calculate the area for any bars still left in the stack
        #the largest area found through both loops is the answer

        maxArea = float('-inf')
        stack = []

        for i, h in enumerate(heights):
            sI = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                sI = index
                maxArea = max(maxArea, height * (i - index))
            stack.append((sI, h))
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea