# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #use DFS to find the path that gets us to the targeted value
        #for each node we come across, subtract its value from whats left, passed through in the parameter
        #we have 2 base cases, one where we reach a None value node, which means that path failed to give us a the sum of the targeted value
        #the other case being if its a leaf node, defined by not having a left or right pointer, return either true or false depending if all the values in the path add up to 0
        
        def dfs(node: TreeNode, nL: int) -> bool:
            if not node:
                return False
            
            if not node.left and not node.right:
                return nL - node.val == 0
            
            nL -= node.val
            
            return dfs(node.left, nL) or dfs(node.right, nL)

        return dfs(root, targetSum)