# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        #create an empty list so we can add onto it throughout the dfs
        res = []

        #go down each branch path and surround the each subtree path with a parenthesis
        def dfs(node: Optional[TreeNode]) -> None:
            nonlocal res

            #if the current node doesn't exist, return to the previous iteration
            if not node:
                return
            
            #add the node's value to the result list
            res.append(str(node.val))

            #if the node has any child, we need to show parentheses for the left side, empty or not
            #this keeps the string correct when indicating a right child with no left child
            if node.left is not None or node.right is not None:
                res.append("(")
                dfs(node.left)   
                res.append(")")

            #only add parentheses for the right child if it actually exists
            if node.right is not None:
                res.append("(")
                dfs(node.right)
                res.append(")")
        
        #initial call to dfs
        dfs(root)

        #condense all list elements into string
        return ''.join(res)
