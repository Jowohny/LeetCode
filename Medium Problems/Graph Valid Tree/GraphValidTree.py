class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        #use a default dictionary populate keys with and default empty list
        #each list will represent the nodes in which the keys are connected to
        connections = collections.defaultdict(list)

        #initialize a deque with the first node
        #since the first node doesn't have a parent node, set it to -1 since there are no nodes that can have the value of -1
        q = deque([(0, -1)])

        #initialize a set with the first node
        #use a set so we don't revisit the same node and reprocess it
        visited = set([0])

        #if there is an equal amount or more of nodes to edges, there there is a loop
        #if the number of edges is less than the number of nodes, then there is a disconnect
        if len(edges) != n-1: 
            return False

        #populate the each of the nodes with their neighbors
        for s, d in edges:
            connections[s].append(d)
            connections[d].append(s)

        #loop until all nodes are processed
        while q:

            #pop the next values off the deque to be processed
            node, parent = q.popleft()

            #go through each of the nodes the current node is connected to
            for nei in connections[node]:

                #if the neighbor isn't the parent node, then continue processing this neighboring node
                if nei != parent:

                    #if we haven't visited this neighboring node, then add it the the deque with the current node as the parent
                    #add the neighbor node to the visited set to avoid reprocessing
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, node))

                    #if we have already visited this node, there there is a loop in the graph, which makes it invalid
                    else:
                        return False

        #if the amount of nodes we have visited isn't the same amount as the given, then there is a disconnect in the graph
        return len(visited) == n