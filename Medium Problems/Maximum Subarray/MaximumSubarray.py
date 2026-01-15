class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        #keep a global max variable to track the maximum sum subarray throughout the traversal of the list
        maxSum = nums[0]

        #dynamically change the current sum value as we interate through the array
        curr = 0

        #interate through every number in the array
        for n in nums:

            #if the current subarray computes a negative, we don't need it so we can cut it off and start back at 0 to find something higher
            if curr < 0:
                curr = 0

            #add the current number to the current subarray value
            curr += n

            #compare the current sum to the global max
            maxSum = max(maxSum, curr)
        
        #after processing all numbers within the array, return the maximum sum subarray
        return maxSum