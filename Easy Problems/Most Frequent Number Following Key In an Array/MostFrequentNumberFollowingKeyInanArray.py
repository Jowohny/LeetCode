class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:

        #create a blank counter object to record frequencies
        freq = collections.Counter()

        #iterate through every number
        for i in range(len(nums)):

            #if the current number is the key, then add 1 to the frequncy of the next number
            if nums[i] == key and i+1 < len(nums):
             freq[nums[i+1]] += 1

        #find and return the most common number that appears after the key
        return freq.most_common(1)[0][0]
        
