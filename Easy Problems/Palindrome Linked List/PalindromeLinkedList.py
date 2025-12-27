# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #use an array to store all the values found within the linked list in order
        res = []

        #traverse through the linked list and add each value
        while head:
            res.append(head.val)
            head = head.next

        #use 2 pointers to represent the first and last index
        l,r = 0,len(res)-1

        #loop until the pointers are overlapping, in this case, lasting about half the length of the list
        while l < r:

            #if at any point in the loop the numbers on either side aren't the same, then it isn't a palaindrome
            if res[l] != res[r]:
                return False

            #bring the pointers inward toward the middle of the array
            l += 1
            r -= 1

        #if the pointers go through the entire loop without return false, then at each point, the numbers were equal, making the linked list a palindrome
        return True
