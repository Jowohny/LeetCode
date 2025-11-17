from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #use a counter to create a list of frequencies
        #go through the key values pairs created by the Counter
        #if any of the values frequencies more than half the length of the list, then return the key

        freq = Counter(nums)
        major = len(nums) // 2

        for k,v in freq.items():
            if freq[k] > major:
                return k