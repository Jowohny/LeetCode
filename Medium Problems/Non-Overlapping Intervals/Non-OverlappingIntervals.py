class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #sort the interval be the last end times
        #keep a variable(removal) to keep track of how many intervals need to be removed
        #initialize another variable with the end time of the first interval as starter
        #go through the intervals starting from the second value
        #check at each interval whether the end of the previous interval overlaps with the start of the current interval
        #if so, then we add 1 to removal as another interval we need to get rid of
        #otherwise, set the prev to the end of the current interval to keep track of the latest end time
        #return the amount we need to remove
        intervals.sort(key=lambda x: x[1])
        removal = 0
        
        prev = intervals[0][1]
        
        for i in range(1, len(intervals)):
            if prev > intervals[i][0]:
                removal += 1
            else:
                prev = intervals[i][1]
        
        return removal
            
            