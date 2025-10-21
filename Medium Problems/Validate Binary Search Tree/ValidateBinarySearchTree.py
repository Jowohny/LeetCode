# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #store each node with its valid value range in queue
        #for a node to be valid, its value must be between the given range, return false otherwise
        #for each left subtree, update the upper bound to the current node’s value
        #for each right subtree, update the lower bound to the current node’s value
        #return true if the queue is empty, meaining all nodes have been processed

        if not root:
            return True

        q = deque([(root, float('-inf'), float('inf'))])

        while q:
            node,left,right = q.popleft()
            if not node:
                continue
            if not (left < node.val < right):
                return False
            if node.left:
                q.append((node.left, left, node.val))
            if node.right:
                q.append((node.right, node.val, right))
            
        return True