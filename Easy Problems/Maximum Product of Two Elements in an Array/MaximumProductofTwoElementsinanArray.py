class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #convert all numbers in the original list to negative
        #by making all the numbers negative, when converting to heap, it makes it a max heap instead of the default min heap
        #pop the top 2 values, subtract both by one and multiply them together and return the result
        nums = [-n for n in nums] 
        heapq.heapify(nums)

        return ((-heapq.heappop(nums))-1)*((-heapq.heappop(nums))-1)