class MedianFinder:

    def __init__(self):

        #initialize a min heap for the larger half of the numbers and a max heap for smaller half of the numbers
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        #always start off by adding the new number into the smaller half
        heapq.heappush(self.small, -num)

        #only initialize check if we half at least one element in the larger half
        #if the largest element in the smaller half is greater than the smallest element in the larger half, then move remove the largest element in the smaller half and move it over to the large half
        if self.large and -self.small[0] > self.large[0]:
            heapq.heappush(self.large, -heapq.heappop(self.small))

        #if the smaller half has less elements than the larger half, then shift some elements over so that the size of the lists even out
        #vice versa, at most, the smaller half of the elements should only have 1 more element than the larger half
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))


    def findMedian(self) -> float:

        #there are more elements in the smaller half than the larger half, then return the largest element in the smaller half of the elements
        if len(self.small) > len(self.large):
            return -self.small[0]

        #if the length of both sides are the same, then take the smallest from the larger side and the largest from the smallest side and divide their sum by 2 to get the median
        return (self.large[0] + -self.small[0])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()