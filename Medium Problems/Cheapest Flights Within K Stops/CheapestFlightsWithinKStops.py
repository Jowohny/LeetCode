from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #create a list of connections defining which flights lead to where
        #use a heap to always pop the path with the least cost every time
        #also use another dictionary to avoid repeating going down the same path (given examples have loops)
        connections = defaultdict(list)
        heap = [(0, 0, src)]
        best = {}

        #fill out the connections for each flight
        for src1, dst1, prc1 in flights:
            connections[src1].append((dst1, prc1))

        #loop if we still have unprocessed flights paths
        while heap:

            #get the path with the least cost from the heap and unpack it
            pathCost, totalFlights, city = heapq.heappop(heap)

            #if the city we have arrived in is the destination, then return the cost of the current path
            if city == dst:
                return pathCost

            #continue to add flights while we have available to use stops
            if totalFlights <= k:

                #loop for each connection this flight has
                for dst2, prc2 in connections[city]:

                    #if we have seen the next path before, check if the cost of the next path is lower than the lowest variation we have of that path
                    #if what we see is higher, then we can ignore it, otherwise, we store the lowest cost in a dictionary for quick access
                    #store the added cost of the next flight along with the amount of stops the current flight path has as well as the city in question
                    if best.get((dst2, totalFlights+1), float('inf')) > pathCost + prc2:
                        best[(dst2, totalFlights + 1)] = pathCost + prc2
                        heapq.heappush(heap, (prc2 + pathCost, totalFlights + 1, dst2))

        #if we can't make it in within the amount of stops, then we return -1
        return -1

                




