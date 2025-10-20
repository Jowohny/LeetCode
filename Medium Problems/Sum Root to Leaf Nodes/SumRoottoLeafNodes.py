# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        #use dfs to explore all paths from root to leaf
        #keep a running string of the current path value as we traverse
        #add the current node value to the path string at each step
        #when we reach a leaf node (no left or right child), convert the full path string into an integer and add it to the total
        #stop recursion when the current node is null
        #after traversing all paths, return the total sum of all numbers formed from root to leaf

        total = 0

        def dfs(node: TreeNode, sn: str) -> None:
            nonlocal total
            if not node:
                return

            sn += str(node.val)

            if not node.left and not node.right:
                total += int(sn)
                return

            dfs(node.left, sn)
            dfs(node.right, sn)
                 
        dfs(root, "")
        return total


