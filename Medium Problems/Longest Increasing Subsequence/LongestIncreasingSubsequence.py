class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        #create a cache so we don't have to recalculate previously found values
        cache = [1] * len(nums)

        #start from the top down and find out how many increasing subsequences are from each point
        for i in range(len(nums)-1, -1, -1):

            #at each point while building backwards, find out how many subsequences there are with the values of this index included
            for j in range(i+1, len(nums)):

                #by using the cache to pull the amount of subsquences from the indexes after the current one, we can continue updating and adding onto the length of the theoretical maximum length
                #only process this number IF the current number is greater than the starting number
                if nums[j] > nums[i]:
                    cache[i] = max(cache[i], 1+cache[j])

        #take the maximum from the entire cache and return the greatest value as it represents the longest increasing subsequence
        return max(cache)

				#really slow but its DP ig...