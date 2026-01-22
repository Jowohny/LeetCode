class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        #initialize a deque starting at the 0th node and a path array with itself in it
        q = deque([(0,[0])])

        #result array used to store all valid paths to the end
        res = []

        #loop until all neighbors for each node are processed
        while q:

            #unpack the front most node in the deque
            node, path = q.popleft()

            #if the node is the last node in the graph, then add the current path to this node to the result
            #if the node is anything else, then add that nodes neighboring nodes along with an update path respective to their node value to the deque
            if node == len(graph)-1:
                res.append(path)
            else:
                for n in graph[node]:
                    q.append((n, path + [n]))

        #return all the possible paths from 0 to n-1 after all nodes have been processed
        return res
            