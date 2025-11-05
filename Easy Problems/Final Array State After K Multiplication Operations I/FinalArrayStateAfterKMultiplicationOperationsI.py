class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        #push all values within the nums list into a heap with its respective index in the original list
        #until we have reached k operations, pop an item off the heap and unpack the value and its index
        #set the value at the index given by the unpacking in the original list to the mupltiplier times itself
        #push the new value onto the heap with its respective index back onto the heap and then decrement k by 1
        #when all operations have been complete, return the list in its final state
        heap = []
        for i, val in enumerate(nums):
            heapq.heappush(heap, (val,i))
        
        while k > 0:
            val, i = heapq.heappop(heap)
            nums[i] = val * multiplier
            heapq.heappush(heap, (val * multiplier,i))
            k -= 1
        return nums