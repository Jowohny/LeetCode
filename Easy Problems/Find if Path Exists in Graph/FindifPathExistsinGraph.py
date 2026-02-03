class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        #use a default dictionary to assign all keys an empty list
        connections = collections.defaultdict(list)

        #create a deque and initialize it with the source of the path
        q = deque([source])

        #create a visited set to avoid processing the same node again
        visited = set()

        #populate the connections with the neighbors of each of the nodes
        for s,e in edges:
            connections[s].append(e)
            connections[e].append(s)
        
        #loop until all nodes in the graph are processed
        while q:

            #pop off the next item in the queue
            node = q.popleft()

            #if the current node is the destination node, then we have found a path that exists
            if node == destination:
                return True
            
            #process each of the current node's neighbors
            for n in connections[node]:

                #only add the neighbor to the queue if they haven't been visited yet
                if n not in visited:
                    visited.add(n)
                    q.append(n)

        #after processing all the nodes without reaching the destination, then there is no path within the given graph
        return False

