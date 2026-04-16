# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

        #use a default dictionary and populate it with lists to define a graph
        #we'll use a graph since in a normal tree, we can only move down, whilst in the graph, we can go in both directions as we'll be making undirected graph with two way connections for each node
        graph = collections.defaultdict(list)

        #use a stack almost like a deque, but pass in the parent and its child node to create the connection
        stack = [(root, None)]

        #create a deque and initalize it with the starting node value
        #since we are using this with the graph, we don't need to pass in the root, only the value
        q = deque([start])

        #use a set so we don't reprocess the infected nodes
        visited = set([start])

        #for time, we start at -1 since the first level its technically at time 0
        time = -1
        
        #loop while there are still connections to be made in the stack
        while stack:

            #pop the item at the top of the stack and unpack them into the node and its parent
            node, parent = stack.pop()

            #if the current node has a parent, AKA not the root node, create a 2 way connection between the given parent and child node
            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)

            #if the current child node has a left/right child node, then add them to the stack with the current node as their parent
            if node.left:
                stack.append((node.left, node))
            if node.right:
                stack.append((node.right, node))

        #loop while there are items in the deque left to be infected
        while q:

            #kind of like frontiers, this loop, the length of the current deque only infects the nodes connected to the last round of nodes
            for _ in range(len(q)):

                #pop off the next node in the deque for processing 
                curr = q.popleft()

                #loop for each of the nodes that are connected to the current node
                for neighbor in graph[curr]:

                    #only process this node if it hasn't been infected or visited(same thing)
                    if neighbor not in visited:
                        
                        #add the neighboring node to the infected/visited set so we don't reprocess this node again
                        #also add neighboring node to the deque to be processed later
                        visited.add(neighbor)
                        q.append(neighbor)

            #increment the time by 1 for each round that passes
            time += 1

        #return the total amount of time it takes to infect all nodes
        return time
