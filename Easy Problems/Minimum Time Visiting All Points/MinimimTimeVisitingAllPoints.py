class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        #create time variable to keep track of how long
        #technically can start at any point so we can just pop the end and deformat to x and y
        #find the max difference between the x and y of 2 point
        #set those as the next points for the next comparison

        time = 0
        x1,y1 = points.pop()
        while points:
            x2,y2 = points.pop()
            time += max(abs(x2-x1), abs(y2-y1))
            x1,y1 = x2,y2
        return time