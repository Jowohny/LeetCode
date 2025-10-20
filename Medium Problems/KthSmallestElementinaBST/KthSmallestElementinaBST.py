# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #use in order traversal since it visits nodes in sorted order for a binary search tree
        #keep a counter to track how many nodes have been visited
        #traverse the left subtree first, then process the current node
        #when the counter matches k, store the current node’s value as the result
        #stop traversal once the element is found
        #return the result after it finishes

        res = 0
        currentK = 0
        
        def inOrderCheck(node: TreeNode) -> None:
            nonlocal res, currentK
            if not node:
                return
                        
            inOrderCheck(node.left)
            currentK += 1
            if currentK == k:
                res = node.val
                return
            inOrderCheck(node.right)
        

        inOrderCheck(root)
        return res