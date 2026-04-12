# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
				#kind of a goofy way to solve this, ill get back to it

        #create a new linked list and assign a dummy node to point to the front of it
        resHead = ListNode()
        dummy = resHead

        #use this list to add all values from the linked list to
        numList = []

        #loop while the current node exists
        while head:

            #add the current value in the linked list to the numList
            numList.append(head.val)

            #iterate to the next node
            head = head.next
        
        #sort the list of numbers in reversed
        numList.sort(reverse=True)

        #loop while there are numbers in the list
        while numList:

            #pop the number at the end of the reversed sorted list(smallest)
            nodeVal = numList.pop()

            #create a new node with the value of the popped number
            resHead.next = ListNode(nodeVal)

            #iterate to the next we just created
            resHead = resHead.next

        #return the node node after the dummy node as that contains our actual final linked list
        return dummy.next

