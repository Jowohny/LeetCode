# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #use BFS to traverse through both lists and check if each value is equal
        #while we have items in the queues, we continue to run until all items have been explored
        #for all items in the queue, pop them and compare values at both queues in the same place
        #if there is a node in one place and none at the other or if the value at the node aren't equal, return false as the trees are no longer equal
        #append all neighboring nodes to the respective queues and continue until all nodes have been processed
        #if both queues are empty by the end, then that mean it has gone through the whole loop without being unequal at all points

        if not p and not q:
            return True
        if not p or not q:
            return False

        q1, q2 = deque(), deque()
        q1.append(p)
        q2.append(q)

        while q1 and q2:
            node1,node2 = q1.popleft(),q2.popleft()

            if not node1 and not node2:
                continue

            if not node1 or not node2 or node1.val != node2.val:
                return False

            q1.append(node1.left)
            q1.append(node1.right)
            q2.append(node2.left)
            q2.append(node2.right)

        if not q1 and not q2:
            return True
        else: 
            return False
