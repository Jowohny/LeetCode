"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #create a set initialized with key pair of None to stand in for any null nodes
        #first pass of the linked list is to create copy off all nodes and also to make sure for the second pass that all nodes exist and can be pointed to
        #the second pass creates the links between nodes as well as the random link between each node
        #we create copies that get put into the hash map, in which we could pull from later and any adjustments made to said copy also made to the copy within the hash
        #return the head referenced in the hash as it contains all the copied nodes
        oldCopy = {None:None}

        curr = head
        while curr:
            copy = Node(curr.val)
            oldCopy[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = oldCopy[curr]
            copy.next = oldCopy[curr.next]
            copy.random = oldCopy[curr.random]
            curr = curr.next

        return oldCopy[head]