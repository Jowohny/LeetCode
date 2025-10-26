"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        #this is quite literally the same as its predecessor, probably easier, so quick explanation
        #if theres no root then then return itself
        #initial a queue with the root
        #store size to tell current loop how long to run for the nodes in the current level
        #use a temporary node to store the prev node
        #for all node that aren't the last node in the level, the next of the stored temporary node to the current node
        #since all nodes orginally have their next set to None, we don't have to do extra work beyond that
        #append the current node's left and right node if they exist
        #after all nodes have been process, return the root
        if not root:
            return root
        
        q = deque([root])
        while q:
            size = len(q)
            temp = None
            for i in range(size):
                node = q.popleft()

                if i < size and temp:
                    temp.next = node
                
                temp = node

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root