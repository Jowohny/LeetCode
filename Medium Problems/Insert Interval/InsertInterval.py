from typing import List

class Solution:
  def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    #there are 3 cases to take into account when coding the solution for this problem
    #the first case scenario would add all intervals with a lesser end time than the new interval start time since they won't interact
    #the second case scenario would be to merge all intervals involved in the new interval
    #for the involved intervals, take into account the max between the start and end of the current interval and the new interval
    #append the result after going through all the involved intervals
    #for the last case scenario, you would need to add all the intervals with a with a greater start time the new intervals end time
    #return the result
    
    result = []
    i = 0
    n = len(intervals)

    while i < n and intervals[i][1] < newInterval[0]:
      result.append(intervals[i])
      i += 1

    while i < n and intervals[i][0] <= newInterval[1]:
      newInterval[0] = min(newInterval[0], intervals[i][0])
      newInterval[1] = max(newInterval[1], intervals[i][1])
      i += 1
    result.append(newInterval)


    while i < n:
      result.append(intervals[i])
      i += 1
            
    return result