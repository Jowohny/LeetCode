class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #find the max number 
        #sort the num list for iteration
        #iterate through the range and compare for loop index and the value in the list
        #if made all the way through, then return len + 1
        nums.sort()

        for i in range(max(nums)):
            if nums[i] != i:
                return i
        return len(nums)