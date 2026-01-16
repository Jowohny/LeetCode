class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #if the cost to get to all the different gas stations are more than what we can get from them, then we don't have the appropriate amount of gas to reach all stations
        if sum(gas) < sum(cost):
            return -1

        #use this to keep track of the net amount of gas we have after the starting index
        #keep the track of the starting index as we move it out the way of the invalid indexes
        netGas = 0
        startIndex = 0

        #loop once for every element in the either of the arrays since they are of the same size
        for i in range(len(gas)):

            #add the difference between the gas we get at the station and the amount of gas it took to get there to the net total of gas
            netGas += (gas[i] - cost[i])

            #if the net gas every dips below 0, then every index before this is invalid since running below 0 would mean we ran out of gas along the way
            if netGas < 0:

                #reset the amount of gas we as need to start at a new index since the last recorded valid index becomes invalid
                netGas = 0

                #set the start index as the index of the next iteration
                startIndex = i + 1
                
        #after reaching the end, return the last recorded valid starting index
        return startIndex