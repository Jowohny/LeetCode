# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #use a DFS to traverse through each node to find the maximum diameter
        #pretty much just how far down the roots can go based on the certain node
        #go as far down on each side as we can and add the length traversed
        #every call down to another node, add 1 to increase the width found
        res = 0

        def dfs(node: TreeNode) -> int:
            nonlocal res 

            if not node:
                return 0

            l = dfs(node.left)
            r = dfs(node.right)
        
            res = max(res, l+r)

            return 1 + max(l,r)
        dfs(root)
        return res
