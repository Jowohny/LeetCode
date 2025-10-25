# Definition for a Node.
# class Node:
#     def __init__(self, val=0, neighbors=None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #check if there is a node present, return None if nothing is found
        #create a dictionary to create copies of clones
        #create a queue and use BFS to traverse through the list
        #initialize inital value of cones with the first node given
        #for every neighbor of the current node, if it hasn't been added to the clone dictionary, then add the node to the queue for further processing
        #after every clone check, add the current neighbor the list of neighbors associated with the node
        #return the clone with the key 'node'
        if not node:
            return None 

        clones = {} 
        q = deque([node])
        clones[node] = Node(node.val)

        while q:
            curr = q.popleft()
            for neigh in curr.neighbors:
                if neigh not in clones:
                    clones[neigh] = Node(neigh.val)
                    q.append(neigh)
                clones[curr].neighbors.append(clones[neigh])

        return clones[node]
