"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        #initial check to see if root exists
        if not root:
            return 0

        #initialize queue with to root to start bfs and a counter to track how many levels there were
        q = deque([root])
        res = 0

        #run while there are nodes available within the queue
        while q:

            #run the for loop for the same amount of nodes found on each level
            for _ in range(len(q)):

                #pop the node off the front of the queue to get its information
                node = q.popleft()

                #if the node exists, add all its children nodes to the queue
                if node:
                    for c in node.children:
                        q.append(c)
            #after each level of nodes have been processed, add 1 to represent the current amount of levels found
            res += 1

        #return the amount of levels after all nodes have been processed
        return res