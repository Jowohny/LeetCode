class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        #find the initial slope of the first 2 coordinates
        (x0,y0), (x1,y1) = coordinates[:2]

        #go through the rest of the coordinates
        for x,y in coordinates[2:]:

            #typical, we would use an equation like (y - y1) / (x - x1) = (y1 - y0) / (x1 - x0), but since we risk a division by zero error, rearrange the equation so there's only multiplication
            if (x1 - x0) * (y - y1) != (x - x1) * (y1 - y0):
                return False

        #if we go through the rest of the coordinates without finding a different slope, then the coordinates display a straight line
        return True
            
	