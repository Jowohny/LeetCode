# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  def detectCycle(self, head: ListNode) -> ListNode:
    #check if the list is empty or only has one node, if so return None
    #create two pointers starting from the head
    #use a while loop to move through the list as long as both pointers are valid
    #move the slow pointer by one step and the fast pointer by two steps each time
    #if the two pointers ever meet, that means there’s a cycle in the list
    #reset the slow pointer back to the head
    #move both pointers one step at a time until they meet again
    #the point where they meet the second time is the start of the cycle
    #if no cycle is found, return None

    slow = head
    fast = head

    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
        slow = head
        while slow != fast:
          slow = slow.next
          fast = fast.next
        return slow

    return None