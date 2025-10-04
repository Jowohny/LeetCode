class Solution:
    def trap(self, height: List[int]) -> int:
        #2 pointers
        #check for local maxes for the left and right
        #increment/decrement based on which side has the shorter height
        #if the height of the current block is less than the local max, it can contain water
        #the amount of water is determined by the current local max minus the current height

        if not height: 
            return 0

        l,r = 0, len(height)-1
        maxLeft, maxRight = 0, 0
        trapped = 0

        while r > l:    
            maxLeft = max(maxLeft, height[l])
            maxRight = max(maxRight, height[r])

            if maxLeft < maxRight:
                trapped += (maxLeft - height[l])
                l += 1
            else:
                trapped += (maxRight - height[r])
                r -= 1
        return trapped
