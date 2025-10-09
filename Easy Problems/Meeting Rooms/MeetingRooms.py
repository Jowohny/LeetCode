"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #sort the interval list in order of the starting time
        #check at each index except the first if the end time of the interval before if greater than the start time of the current interval
        #if it is greater, then there are no conflicts
        #if it is lesser, then there is a conflict
        intervals.sort(key=lambda x: x.start)
        if len(intervals) <= 1:
            return True

        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False

        return True
