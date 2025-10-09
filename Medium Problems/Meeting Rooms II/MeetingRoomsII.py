"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #sort the intervals by start time
        #create a minheap and append the first end time in the list of intervals
        #go through the intervals list and check if the current start time is at least greater or equal to the first element in the minheap
        #if it is greater or equal to, then pop off the first element on heap
        #after each check, add the current end of the interval to the heap
        #return the length of the heap
        
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)
        minHeap = []
        heapq.heappush(minHeap, intervals[0].end)
        
        for i in range(1, len(intervals)):
            if intervals[i].start >= minHeap[0]:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, intervals[i].end)
        
        return len(minHeap)
