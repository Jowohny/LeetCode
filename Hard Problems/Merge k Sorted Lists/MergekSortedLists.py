# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #do an initial check if the list has no elements or doesn't exist
        #basic game plan, merge lists together in pairs of 2 until we reach 1 which should contain our total list
        #to do so, we use a while loop to run through the length of the lists
        #every iteration, we merge 2 lists at a time, reducing the amount
        #we merge based on the value given from the nodes, add in terms of which value is smaller
        #after each iteration, set the lists value to the to new list to update the length of the while loop 
        #when the length of the lists becomes 0, it means that we have merged all lists into 1 so return the first list
        if len(lists) == 0 or not lists:
            return None

        while len(lists) > 1:
            sortedLists = []
            for i in range(0,len(lists),2):
                list1 = lists[i]
                list2 = lists[i+1] if (i+1) < len(lists) else None
                if list2 is None:
                    sortedLists.append(list1)
                    continue
                sortedLists.append(self.mergeLists(list1,list2))
            lists = sortedLists
        return lists[0]

    def mergeLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val > list2.val:
                tail.next = list2
                list2 = list2.next
            else:
                tail.next = list1
                list1 = list1.next
            tail = tail.next
            
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
            
        return dummy.next

