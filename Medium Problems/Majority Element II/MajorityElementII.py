class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        #create a frequency list with all the numbers in the given list
        freq = collections.Counter(nums)

        #only return the numbers whose frequencies are greater than 1/3 the size of the list
        return [n for n,f in freq.items() if f > len(nums)/3]