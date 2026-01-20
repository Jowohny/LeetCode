class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        #use a counter to create a frequency list of all the numbers in the list
        freq = collections.Counter(nums)

        #iterate through each item in the frequency list
        for n,f in freq.items():

            #if the current item's freqency is 1, then return the number since we are only guarenteed one singly occuring item
            if f == 1:
                return n