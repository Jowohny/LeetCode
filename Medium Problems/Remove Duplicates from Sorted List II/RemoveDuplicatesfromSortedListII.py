# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #create a dummy node to reference the start of the list
        dummy = ListNode()

        #use a traveling node to indicate where thee end of the list is for ease of adding new nodes
        travel = dummy

        #loop until we have reached the end of the linked list
        while head:

            #if there is a node that exists after the current one and they happen to be the same value, skip the repeating values until the next value is no longer the same
            if head.next and head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next

            #if the current node is the final node of the linked list or the current and the next nodes aren't the same value, create a new node and add it to our final linked list
            #shift the traveling node to the new end of the linked list
            elif not head.next or head.val != head.next.val:
                travel.next = ListNode(head.val)
                travel = travel.next

            #update the pointer to the next node
            head = head.next

        #since we haven't moved the dummy node anywhere in the list, it is still referencing the beginning
        return dummy.next

            
            

            