# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        #use dfs to explore all paths from the root to the leaf nodes
        #start with an empty string to build each path as we go deeper
        #for each node, add its value to the current path
        #if the node is a leaf (no left or right child), store the full path in the result list
        #otherwise, keep traversing left and right children while adding '->' between nodes
        #after finishing all recursive calls, return the list of all completed paths

        res = []
        
        def dfs(node: TreeNode, path: str) -> None:
            nonlocal res
            if not node:
                return
        
            if not node.left and not node.right:
                res.append(path + str(node.val))
            
            dfs(node.left, path + str(node.val) + '->')
            dfs(node.right, path + str(node.val) + '->')
        
        dfs(root, "")
        return res
            