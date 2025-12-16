class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #create the heap to keep the elements closest to x at the top and a result to push the associated number into
        closest = []
        res = []

        #take the absolute value of the difference between each number in the array and x
        #push difference integer pair into the heap
        #pushing into the array with the difference as the key
        for n in arr:
            heapq.heappush(closest, (abs(x-n), n))
        
        #pop values off the heap k times and append them into the result array
        for _ in range(k):
            num = heapq.heappop(closest)[1]
            res.append(num)

        #sort result array so it is in ascending order
        res.sort()

        #return the result array
        return res