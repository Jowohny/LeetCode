# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #create a node before the head so we can reference the head later with less issues, and another to traverse through the linked list, referenced to the original dummy node
        dummy = ListNode(0, head)
        prev = dummy

        #walk prev forward until it sits right before the first node we need to reverse
        for _ in range(left - 1):
            prev = prev.next

        #grab the last node of the section we need to reverse by stepping through the section length
        kth = prev
        for _ in range(right - left + 1):
            kth = kth.next

        #grab the node after the section for reconnecting the linked list later
        groupNext = kth.next

        #create 2 more nodes, in which both point to the node that represents the start of the section, one will be keeping track of the node previously processed and the other to traverse
        curr = nextPrev = prev.next

        #create 1 more node in which its purpose is to connect the node to the current end of the section
        prevNode = groupNext

        #we continue until we reach the end of the current section
        while curr != groupNext:

            #to reverse the section of nodes, we store the node after the current one, point the current node to the node after the section
            #after redirecting the current node, use a variable to iterate back to the redirected node so we know what to point the next node to
            #set the current node to the stored node from earlier, representing the next node we need to point the current end of the section
            temp = curr.next
            curr.next = prevNode
            prevNode = curr
            curr = temp

        #connect the node before the section to the node that was previously at the end of the section, stitching everything back together
        prev.next = kth

        #the dummy node represents the node before the head, so all changes that have been made are referenced in the node after the dummy
        return dummy.next
