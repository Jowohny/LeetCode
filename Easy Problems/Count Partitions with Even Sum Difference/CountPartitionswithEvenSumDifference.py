class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        #keep a counter to record how many partitions of even difference
        total = 0

        #go through all the different partitions
        for i in range(1,len(nums)):
            #get the sum of each side and subtract, check if they are even or odd
            #if the different is even, then increment the total counter
            if (sum(nums[:i]) - sum(nums[i:]))%2 == 0:
                total += 1

        #after all partitions have been calculated, return the amount of even difference partitions
        return total