class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        #use a set to track which nodes we have already visited to avoid reprocessing
        visited = set()

        #create a list of connections for each node paired with their success probabilites
        connections = collections.defaultdict(list)

        #use a max heap(negative numbers) to extract the highest probabilies at the current stage in the heap
        heap = [(-1.0, start_node)]


        #since we are dealing with undirected graphs, we need to create a 2 way connection for each node
        for i,(e1,e2) in enumerate(edges):
            connections[e1].append((succProb[i], e2))
            connections[e2].append((succProb[i], e1))

        #loop until we either run out of nodes to process or until we have reached the end node
        while heap:

            #pop the node with the highest probability from the heap and unpack it
            prob, dNode = heapq.heappop(heap)

            #only process the node if it hasn't been visited previously
            if dNode not in visited:

                #mark the node as visited
                visited.add(dNode)

                #if the current node is the end node, then return the probability
                if dNode == end_node:
                    return -prob

                #process all nodes connected to the current node
                for prob1, dNode1 in connections[dNode]:

                    #only add onto the heap it the connected nodes haven't been visited yet
                    if dNode1 not in visited:

                        #multiply the current probability with the probability of the next node before adding onto the heap
                        heapq.heappush(heap, (prob1*prob, dNode1))

        #if we went through the entire heap without landing on the end node, the given end node is unreachable
        return 0.0