# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        #we drop the linked list values into an m by n grid while spiraling inward, and any leftover cells stay as -1
        #start the grid filled with -1 so the empty cells are already handled once the list runs out
        #keep four boundaries, top and bottom rows and left and right columns, that close in as we go
        #walk left across the top row, down the right column, back across the bottom, then up the left column
        #after finishing each side pull that boundary in one step, and stop the moment the linked list is empty

        #grid starts as all -1, the values we place will overwrite whats needed
        matrix = [[-1] * n for _ in range(m)]

        #the four edges of the part of the grid we still need to fill
        top, bottom = 0, m - 1
        left, right = 0, n - 1

        while head and top <= bottom and left <= right:

            #walk left to right across the top row
            for c in range(left, right + 1):
                if not head:
                    break
                matrix[top][c] = head.val
                head = head.next
            top += 1

            #walk top to bottom down the right column
            for r in range(top, bottom + 1):
                if not head:
                    break
                matrix[r][right] = head.val
                head = head.next
            right -= 1

            #walk right to left across the bottom row
            for c in range(right, left - 1, -1):
                if not head:
                    break
                matrix[bottom][c] = head.val
                head = head.next
            bottom -= 1

            #walk bottom to top up the left column
            for r in range(bottom, top - 1, -1):
                if not head:
                    break
                matrix[r][left] = head.val
                head = head.next
            left += 1

        return matrix
