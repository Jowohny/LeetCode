# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        #if the root doesn't exist, return 0 since theres no depth
        #add the nodes to the queue with a with an associated depth attached 
        #we run the tree through a loop until there exists a node that doesn't have any children
        #until then, we add the children of each node to the queue and wait for them to be processed

        if not root:
            return 0
        
        q = deque([(root, 1)])
        
        while q:
            node, depth = q.popleft()
            
            if not node.left and not node.right:
                return depth
            
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))