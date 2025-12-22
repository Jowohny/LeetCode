class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        #create a negated version of the pile list so it creates a max heap when heapifying
        maxHeap = [-p for p in piles]
        heapq.heapify(maxHeap)

        #run loop k amount of times
        for _ in range(k):
            
            #pop the biggest pile off the heap and put it back onto the heap after performing the operation
            pile = -heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, -(pile-int(pile/2)))
        
        #return the negated sum of the values left in the heap
        return -sum(maxHeap)
