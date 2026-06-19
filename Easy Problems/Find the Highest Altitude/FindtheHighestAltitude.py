class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        #create 2 variables, one to keep track of the current altitude and another to record the highest found altitude
        highest = 0
        current = 0

        #loop through the list of elevation changes
        for i in gain:

            #add the elevation change to the current altitude variable
            current += i

            #compare the current altitude to the highest found one and keep the higher altitude between the two
            highest = max(highest, current)

        #after going through all the elevation changes, return the highest found altitude
        return highest