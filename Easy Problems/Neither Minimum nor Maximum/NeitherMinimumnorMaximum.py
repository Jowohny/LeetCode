class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:

        #find the the maximum number from the list and find the minimum number from the list
        listMax = max(nums)
        listMin = min(nums)

        #iterate through every number in the list
        for n in nums:

            #if the current number is the maximum or minimum number we found earlier it has to be something in between, so return that number
            if n != listMax and n != listMin:
                return n
            
        #returning this mean that the list was too small, meaning a list size less than 3
        return -1