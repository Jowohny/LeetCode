# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #keep one pointer to track the reversed portion and use another pointer to traverse through the original list
        #for each node, store its next node, then reverse the link
        #move previous pointer to the current node and send the current node to the next
        #continue until the current node is set to nothing
        #return at the previous pointer since it will point to the new head of the reversed list

        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev