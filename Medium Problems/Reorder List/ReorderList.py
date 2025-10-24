# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #initially use a fast and slow pointer to find the middle of the list
        #when the fast pointer reaches the end of the linked list, the slow pointer at or around the middle
        #in order to start reordering, we need to reverse the second half of the list
        #to reverse, store temperary and a previous node, store the next node temporarily, point the current node to the previous node, set the previous node to the current node which updates it, and then set the the current node to the temporary node, restoring the link
        #after reversing the second half, use 2 pointers, one at the start of the linked list and another at the start of the reversed portion of the linked list
        #to merge, store 2 temporary nodes, use the temporary nodes to store what the pointers on each side are pointing too, set the beginning node to point to the last node, and set the last node to point to what the first node was pointing at before, restoring the link, then update both pointers with the temporary values
        slow,fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        first,second = head,prev
        while second:
            temp1,temp2 = first.next,second.next
            first.next = second
            second.next = temp1
            first,second = temp1,temp2