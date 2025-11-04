class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #for all the coordinates in the list, find the distance and pair it with the coordinates in the heap
        #make the distance negative so when we store in the heap, it effectively becomes a max heap
        #if the amount of items on the heap become more than the given k, pop the furthest points 
        #return a list of all the coordintates left in the heap
        maxHeap = []
        for x,y in points:
            distance = -(x**2+y**2)
            heapq.heappush(maxHeap, (distance, [x,y]))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        return [coor for _,coor in maxHeap]


