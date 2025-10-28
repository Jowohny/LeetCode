# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #do an initial check on if the head exists or if it points to another node
        #run through the array initial to find out how long it the total list is
        #perform an operation to see how much to actually rotate
        #use another node to point to the place where we need to splice
        #when at the location, save the next node as the place where the new head is supposed to be
        #after that, set the next node to none, since it is still linked to the head, it'll cut off the original list
        #referencing our new head located at the place of the cut off, set the end of that cutoff list to point to the original cut off list
        #return the new head node

        if not head or not head.next:
            return head

        l = 1
        tail = head
        while tail.next:
            tail = tail.next
            l += 1
        
        k = k%l
        if k == 0:
            return head
        
        newTail = head
        for _ in range(l-k-1):
            newTail = newTail.next
        
        newHead = newTail.next
        newTail.next = None
        tail.next = head

        return newHead