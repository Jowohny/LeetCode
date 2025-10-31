class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #do an inital check to see if a list with vales even exists
        #heapify the list to arrange it in a min heap, in this case, increasing order
        #when we go to pop the numbers from the heapified list, which since we are taking numbers from the back, it essentially reverse the list to decreasing order
        #return the result after all the numbers in the orginal array gets popped
        if not nums:
            return []

        res = []
        heapq.heapify(nums)
        while len(nums) != 0:
            res.append(heapq.heappop(nums))
        return res
