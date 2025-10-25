# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #check if either of the lists are empty, return None if so
        #create two pointers to traverse through both lists
        #use a while loop to keep moving both pointers until they meet
        #if a pointer reaches the end of its list, switch it to the head of the other list
        #this way, both pointers will eventually align and cover equal total distance
        #if the two pointers meet, that node is the intersection point
        #if both pointers reach the end (None) without meeting, it means there is no intersection
        #return the node where they meet or None if no intersection is found

        if not headA or not headB:
            return None

        currA, currB = headA, headB

        while currA != currB:
            if currA is None:
                currA = headB
            else:
                currA = currA.next
                
            if currB is None:
                currB = headA
            else:
                currB = currB.next
            

        return currA 