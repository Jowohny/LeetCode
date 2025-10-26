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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        #do an initial check to see if there is a root or not
        #use a queue initialized with the root to perform BFS to go through the tree level by level
        #use a temporary node to know the previous node and set its next value to the current node
        #when the current node reaches the size of the list, set its next value to None
        #append the current node's left and right node if they exist 
        #after all nodes have been processed, return the root

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
                else:
                    node.next = None

                temp = node
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root

                