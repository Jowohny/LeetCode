class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort the intervals so the start times are in ascending order
        #append the first interval to the resulting loop
        #unpack the intervals into a start and end varable
        #in the last interval of the resulting array, check if the end of that is greater or equal to the start of the current interval
        #if the condition passes, set the end of last interval in the resultant array to the max between the current end and the last result end
        #otherwise append the next start and end into the result
        #return the result
        
        intervals.sort()
        res = [intervals[0]]
        
        for start, end in intervals:
            if res[-1][1] >= start:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])
        
        return res