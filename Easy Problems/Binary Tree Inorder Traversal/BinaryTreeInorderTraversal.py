# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #create a list to add all values
        #go to the lestmost node in each subtree
        #add the value of the root to the result array before the left most node
        #repeat for every node going down the right subtrees

        res = []

        def inOrder(node: TreeNode) -> None:
            nonlocal res
            if not node:
                return

            inOrder(node.left)
            res.append(node.val)
            inOrder(node.right)
        
        inOrder(root)
        return res