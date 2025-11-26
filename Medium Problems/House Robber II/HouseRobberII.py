class Solution:
    def rob(self, nums: List[int]) -> int:
        #keep sets of variables seperate for each version of the list we are using
        #just like house robber, we are trying to get the most money except this one is connected from the front and the back of the list
        #to work around it, run through a version of the list where the first house is excluded and another where the list house is exluded
        #that way there is no issues with the wrap around
        #for each version, compare the added value of the current house and the house stored 2 blocks away to the house right before
        #take the greater value, and store it in the value of the previous house, which will represent the max for values before that index
        #update the value of the house 2 block away to the one right before
        #after both versions are done, compare the them alongside the first index of the list in the case that there are insufficient values in the list
        #return the max value between them

        house1i, house2i = 0,0
        house1j, house2j = 0,0

        for n in nums[1:]:
            temp = max(n+house1i, house2i)
            house1i = house2i
            house2i = temp

        for n in nums[:-1]:
            temp = max(n+house1j, house2j)
            house1j = house2j
            house2j = temp

        return max(nums[0], house2i, house2j)