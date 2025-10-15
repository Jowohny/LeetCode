# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #initialize two pointers at the start of the linked list
        #move the fast pointer ahead by n steps to create a gap
        #move both pointers one step at a time until fast is at the last node
        #slow pointer will now be right before the node that needs to be removed
        #skip over slow's next node by setting the next value to the value after next node
        #return the updated head of the list

        fast,slow = head,head

        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return head