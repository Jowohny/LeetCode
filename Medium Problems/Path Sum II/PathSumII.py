# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        #use DFS to find a direct path to a leaf node
        #if there is no node passed into the paraters, that is the base case
        #if the current node is no the leaf node, add the val to the current path sum and add the current node value to the path array
        #if the current node is a leaf node, check if the sum of the current path is the same as the target
        #if the path sum is the same, then return the path that led to that sum
        #backtrack by removing the last node if path is unsuccessful
        
        res = []

        def dfs(node: Optional[TreeNode], path: List[int], currSum: int) -> None:
            if not node: 
                return
            
            currSum += node.val
            path.append(node.val)

            if not node.left and not node.right and currSum == targetSum:
                res.append(path[:])
            
            dfs(node.left, path, currSum)
            dfs(node.right, path, currSum)
            path.pop()
        
        dfs(root, [], 0)
        return res