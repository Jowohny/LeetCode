# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #create a helper function that recursively goes through the tree in desired order
        #in this case, we want to add the value of the current node before going to the next ones
        #keep traveling through the tree until all subtrees have been processed
        #return the result array that should have the proper int order
        
        res = []

        def preOrder(node: TreeNode) -> None:
            nonlocal res
            if not node:
                return

            res.append(node.val)
            preOrder(node.left)
            preOrder(node.right)
        
        preOrder(root)
        return res