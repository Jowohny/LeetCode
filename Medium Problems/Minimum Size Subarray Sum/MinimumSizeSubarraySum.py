class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #use a sliding window to find the smallest subarray in which its sum is greater than the target
        #we start both pointers at index 0
        #we use the right pointer to traverse through the values to add the current sum of the window until the window's sum reaches the target value
        #when then increment the index of the left pointer and take away the value at the pointer from the sum until we see that the window sum becomes less than the target
        #when incrementing the left pointer, take the minimum between the current window length and the current most minimum length found
        #return 0 when there has been no window found in which the sum of its components are greater or equal to the target
        #otherwise return the minimum length

        minLen = float('inf')
        l = 0
        currSum = 0

        for r in range(len(nums)):
            currSum += nums[r]

            while currSum >= target:
                minLen = min(minLen, r-l+1)
                currSum -= nums[l]
                l += 1
                
        if minLen == float('inf'):
            return 0
        else: 
            return minLen