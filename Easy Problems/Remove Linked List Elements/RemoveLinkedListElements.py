# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #use a dummy node that points to the head of the linked list to handle edge cases cleanly
        #set a pointer to start from the dummy node so we can move through the list safely
        #while answer is not None, check if the next node exists and whether its value matches the given val
        #if it matches, skip that node by pointing answer.next to answer.next.next which removes the next node
        #if it doesn’t match, move the pointer forward to the next node
        #continue until all nodes have been checked and removed if necessary
        #return dummy.next since dummy is a placeholder and the actual list

        dummy = ListNode(0, head)
        answer = dummy

        while answer:
            while answer.next and answer.next.val == val:
                answer.next = answer.next.next
            answer = answer.next
        
        return dummy.next