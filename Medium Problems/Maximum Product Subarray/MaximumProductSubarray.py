class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        #change accordingly to the greatest current max
        result = max(nums)

        #since we don't need the actual subarray, we can just save the space and keep the smallest found minimum and the largest found maximum
        globalMin, globalMax = 1, 1

        #loop through every number the the given list
        for n in nums:

            #every number in the list we process, we find the essentially finding the maximum and minimum from all the subarrays that can be made from said processed numbers
            values = [n, n*globalMax, n*globalMin] 

            #update the global minimum and the global maximum to represent the extremes on each end
            #we keep minimums just in case there's a negative number, in the case that there is a another negative number, it could multiply into a bigger positive number
            globalMin = min(values)
            globalMax = max(values)

            #compare the global maximum and the previous recorded result and update as necessary
            #no need to add the global minimum for comparison, for obvious reasons
            result = max(globalMax, result)

        #return the highest found maximum
        return result

        