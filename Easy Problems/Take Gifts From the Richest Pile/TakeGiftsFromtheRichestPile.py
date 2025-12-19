class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        #use this as the final counter of all the remaining gifts after all operations
        res = 0

        #create a negated version of the gift list so it becomes a maxHeap when heapifying
        maxHeap = [-g for g in gifts]
        heapq.heapify(maxHeap)

        #pop the pile with the greatest amount of gifts, square root them, then add them back in the heap
        for t in range(k):
            curGift = -heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, -int(math.sqrt(curGift))) 

        #after all rooting operations, unnegate the gift amount and add them to the result
        for g in maxHeap:
            res += -g

        #return the amount of remaining gifts after all operations
        return res