class Solution:
    def rob(self, nums: List[int]) -> int:
        #use 2 variables to track the current state of the houses as we traverse through the list
        #at each step, compare the values of the current house added with the house 2 indexes away and the previous house on its own
        #we do this because the variable that stores the house 2 indexes away can be added with due to them not being next to each other
        #on the other hand, when using the previous house from the current one, it can't be added with either one of the houses since its next to both of them
        #at each step we update the housing situation by moving them up a block while other house that comes before the current hold the values of the max values of the rest of the subset before it
        #knowing that, when we rob all the houses, we return the value found in the variable that stores the second house as it hold the solved values of the whole set

        house1, house2 = 0,0

        for n in nums:
            temp  = max(n + house1, house2)
            house1 = house2
            house2 = temp
        return house2