from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        #impliment dijkstras algorithm
        #we need to make a dictionary defining which nodes connect to who
        #create a visited set so we don't repeat processing nodes that have already been visited
        #use a heap to interatively find the minimum time between all the current found paths
        #keep a counter to as a measure to how long it takes for all nodes to receive a signal
        connections = defaultdict(list)
        visited = set()
        heap = [(0,k)]
        time = 0

        #unpack all the variables into the node, the node it connects to, and the weight that connection has
        for u,v,w in times:
            connections[u].append((v,w))
            
        #loop until all nodes within the network have been processed
        while heap:

            #pop the pop off the heap with the lowest cost and unpack it into its path weight and its current node
            w1, n1 = heapq.heappop(heap)

            #only process the popped node if it hasn't been explored yet
            if n1 not in visited:

                #add the current node to the visited set so we don't process it again later
                visited.add(n1)

                #the time would be set the the length of the current shortest path
                time = w1

                #loop through the connections that the current node has
                for n2, w2 in connections[n1]:

                    #only add the neighboring nodd if we haven't visited yet
                    #when pushing the neighbors onto the heap, we need to push the total weight of the path so far instead of just the weight of the path itself
                    if n2 not in visited:
                        heapq.heappush(heap, (w1+w2, n2))

        #only return the time if we were able to visit every single node in the network, return -1 otherwise
        return time if len(visited) == n else -1

        