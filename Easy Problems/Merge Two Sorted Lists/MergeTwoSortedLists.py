# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #have a pointer for each of the lists 
        #if we see that a value on one side greater than the other
        #add value to the resultant node and incriment that pointer
        #return final result when both lists are out of elements
        curr = res = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                curr.next = list1
                curr = list1
                list1 = list1.next
            else:
                curr.next = list2
                curr = list2
                list2 = list2.next
                
        if list1 or list2:
            if list1:
                curr.next = list1
            else:
                curr.next = list2
            
        return res.next