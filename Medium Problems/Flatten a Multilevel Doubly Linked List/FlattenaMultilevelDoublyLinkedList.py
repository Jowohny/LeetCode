"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        #if there is no head, then there's nothing to flatten
        if not head:
            return head

        #set a sentinal node to return later while we traverse with the head
        dummy = head

        #loop only if the current head is valid
        while head:

            #if the current head has a child node, save the node that comes next on the same level and start traversing through the child nodes
            #connect the child node to the parent by pointing the the parent node to the head of the child layer and setting the previous of the child head to the parent
            #after connecting them, remove the original children as they are already connected to the main line
            if head.child:
                nextNode = head.next
                childHeadNode = head.child

                head.next = childHeadNode
                childHeadNode.prev = head
                head.child = None

                #find the last node of the current child layer
                lastChildNode = childHeadNode
                while lastChildNode.next:
                    lastChildNode = lastChildNode.next

                #connect the last node of the child layer to the node that the parent was originally pointing to before
                lastChildNode.next = nextNode

                #if the parent node originally pointed to another node, make sure to have that node have its previous point to the last child node
                if nextNode:
                    nextNode.prev = lastChildNode

            #iterate to the next node
            head = head.next

        #return the original sentient node
        return dummy
            