class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        #initialize a result variable to store the total number of slices found and another to track the current number of combinations
        #start the loop from the third element since a valid arithmetic slice needs at least three numbers
        #at every index, check if the difference between the current and previous element is equal to the difference between the previous two elements
        #if the differences are equal, increment the current combination count and add it to the result
        #this works because each new number extending the arithmetic pattern which creates more subarrays within the sequence
        #if the pattern breaks, reset the current combination count to 0
        #return the total count of arithmetic subarrays after the loop ends

        res = 0
        curCom = 0

        for i in range(2,len(nums)):
            if nums[i-1] - nums[i] == nums[i-2] - nums[i-1]:
                curCom += 1
                res += curCom
            else:
                curCom = 0
        return res