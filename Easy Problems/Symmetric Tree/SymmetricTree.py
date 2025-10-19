# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #create two queues, one for each side of the tree
        #if the values immediate to the root arent equal, then the whole tree won't be equal
        #while we have items in the the queues, check if both of the current nodes exist or are equal in value
        #if any of those conditions come out to be false, return False
        #otherwise, add all neighbors either outside to in or inside to out
        #if you run through the entire while loop, that means all nodes have been explored and found to be equal

        q1,q2 = deque([root.left]),deque([root.right])

        if not root.right and not root.left:
            return True

        if not root.left or not root.right or root.left.val != root.right.val:
            return False

        while q1 and q2:
            node1,node2 = q1.popleft(),q2.popleft()

            if not node1 and not node2:
                continue

            if not node1 or not node2 or node1.val != node2.val:
                return False

            q1.append(node1.left)
            q1.append(node1.right)
            q2.append(node2.right)
            q2.append(node2.left)

        
        return True