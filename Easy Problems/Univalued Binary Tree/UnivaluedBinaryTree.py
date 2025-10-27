# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        #do an initial check for if the root has an child nodes
        #use the root value to check if all other values are the same
        #use a queue to interate through the tree using BFS
        #for every node, compare each of their values to the root node value, if theres one value that different, then the univalued factor is invalid
        #if there exists a left or right node, add them to the queue
        #once we exit the loop, it means that we have processed all node and have found that all node values are the same
        if not root.left and not root.right:
            return True
        
        q = deque([root])
        uni = root.val
        while q:
            node = q.popleft()
            if node.val != uni:
                return False
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return True
        