class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        #use a default dictionary and populate the keys with their own empty list
        connections = collections.defaultdict(list)

        #use a visited set to avoid reprocessing the same node again
        visited = set()

        #intialize a deque
        q = deque()

        #track the amount of disconnected pieces there are in the graph
        components = 0

        #populate each node with their respective neighbors
        for s, d in edges:
            connections[s].append(d)
            connections[d].append(s)

        #implemented bfs in seperate function for better readability
        def bfs():

            #loop until all the nodes from this component are processed
            while q:

                #pop the next node off the deque to be processed
                node = q.popleft()
                
                #go through each of the this nodes neighbors
                for nei in connections[node]:

                    #if this neighbor hasn't been visited, add it to the deque to be processed
                    #also add it to the visited set so we don't revisit it again 
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)

        #go through each of the nodes to catch every possible component
        for i in range(n):

            #if the current node hasn't already been visited through the bfs algorithm, then add it to the deque
            #also add it to the visited set so we don't process it again
            #add 1 to the total amount of components
            #call the bfs method with the new starting node in the deque
            if i not in visited:
                visited.add(i)
                q.append(i)
                components += 1
                bfs()

        #after all nodes have been processed, return the total amount of disconnected pieces in the graph
        return components
