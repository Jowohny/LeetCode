# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #create a helper function that recurses through the entire tree in the desired order
        #append the current value of the node to the result array after it has finished recursing
        #
        res = []

        def postOrder(node: TreeNode) -> None:
            nonlocal res 
            if not node:
                return
            
            postOrder(node.left)
            postOrder(node.right)
            res.append(node.val)

        postOrder(root)
        return res