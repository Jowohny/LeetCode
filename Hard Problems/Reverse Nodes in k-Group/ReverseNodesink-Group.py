# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #create 2 nodes, one before the head so we can reference the head later with less issues, and another to traverse through the linked list, refernced the to the original dummy node
        dummy = ListNode(0, head)
        prev = dummy

        #grab the intial group of nodes we need to reverse through the helper
        kth = self.getKth(prev, k)

        #the loop continues based on whether the kth node exists, calculated after every loop
        while kth:
            #grab the node after the group for reconnecting the linked list later
            groupNext = kth.next

            #create 2 more nodes, in which both point to the node the represents the start of the group, one will be keeping track of the node previously processed and the other to traverse
            curr = nextPrev = prev.next

            #create 1 more node in which its purpose is to connect the node to the current end of the group
            prevNode = groupNext

            #we continue until we reach the end of the current group
            while curr != groupNext:

                #to reverse the group group of nodes, we store the node after the current one, point the current node to the node after the group
                #after redirecting the current node, use a variable to interate back to the redirected node so we know what to point the next node to
                #set the current node to the stored node from earlier, representing the next node we need to point the current end of the group
                temp = curr.next
                curr.next = prevNode
                prevNode = curr
                curr = temp

            #connect the the node before the group to the node that was previously at the end of the group, then move the pointer to the end of the group for the next batch of k nodes
            prev.next = kth
            prev = nextPrev

            #find the next group to reverse
            kth = self.getKth(prev, k)

        #the dummy node represents the node before the head, so all changes that have been made are referenced in the node after the dummy
        return dummy.next

    def getKth(self, node, k):

        #interate through the node k times, if there arent enough nodes, then the kth node with be returned as None, meaning we reached the end
        while node and k > 0:
            node = node.next
            k -= 1
        return node
