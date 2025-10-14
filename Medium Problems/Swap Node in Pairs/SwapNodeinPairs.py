# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        #check if the list is empty or has only one node, in which case no swap is needed
        #if there are at least two nodes, store the second node in a temperary node variable
        #recursively call the function for the rest of the list starting from the third node
        #set the next of the first node to point to the result of the recursive call
        #set the next of the temperary node to point back to the first node
        #return the temperary node as the new head after the swap

        if not head or not head.next:
            return head
        
        temp = head.next  
        head.next = self.swapPairs(temp.next)
        temp.next = head  
        
        return temp