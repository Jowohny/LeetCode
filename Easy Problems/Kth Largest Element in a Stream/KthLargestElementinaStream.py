class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #convert the number list into a heap
        self.nums = nums
        heapq.heapify(nums)

        #globalize k
        self.k = k

        #if the length of the number list is greater than the given k, then keep popping from the list until equal to or less than
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        

    def add(self, val: int) -> int:
        #add the value onto the heap
        heapq.heappush(self.nums, val)

        #if the added value makes the length of the list higher than k, then pop a value from the list
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        
        #the small value in the heap is the first value
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)