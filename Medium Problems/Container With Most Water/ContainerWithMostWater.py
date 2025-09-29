class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        #the area of the container will be the height of the lower wall times the difference in index
        #use a variable to keep track of the container with the most water
        #incriment either side of the wall based on which wall is shorter

        maxArea = 0
        l,r = 0, len(heights)-1
        while l<r:
            currentMax = min(heights[l], heights[r]) * (r-l)
            maxArea = max(maxArea, currentMax)
            if heights[l] > heights[r]:
                r-=1
            elif heights[l] < heights[r]:
                l+=1
            else:
                l+=1
        return maxArea