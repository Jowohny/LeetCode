"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        #check if the root exists
        if not root:
            return []

        #initialize a queue with the root node along with a list to store all the levels in
        q = deque([root])
        res = []

        #we don't stop until all the nodes in the tree are processed
        while q:

            #store all the nodes in the current level within the list
            level = []
            for _ in range(len(q)):
                #get the current node in the current level
                node = q.popleft()

                #add the value of the current node to the current level list
                level.append(node.val)

                #add all the children from the nodes current level to be processed later for the next level
                for c in node.children:
                    q.append(c)

            #append all the values of the current level to the result list
            res.append(level)

        #return the level order traversal after all nodes are processed
        return res