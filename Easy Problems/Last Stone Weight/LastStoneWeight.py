class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #rewrite the whole list to that every value is negative
        #heapify the list so that the list becomes a max heap
        #until the list becomes size 1, pop the 2 biggest stones and take the difference
        #push the difference into the stack
        #when the size of the list becomes 1, return the only value in the heap
        stones = [-s for s in stones] 
        heapq.heapify(stones)
        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            if stone2 > stone1:
                heapq.heappush(stones, stone1-stone2)
        stones.append(0)
        return abs(stones[0])

