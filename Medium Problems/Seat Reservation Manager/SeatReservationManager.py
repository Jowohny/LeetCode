class SeatManager:

    def __init__(self, n: int):

        #create the range of seats from 1 - n and heapify it to do the intial set up
        self.heap = [i for i in range(1,n+1)]
        heapq.heapify(self.heap)

    def reserve(self) -> int:

        #pop the reservation with the lowest number value off the heap and return it
        return heapq.heappop(self.heap)
        

    def unreserve(self, seatNumber: int) -> None:
        #push the number being unreserved back onto the heap
        heapq.heappush(self.heap, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)