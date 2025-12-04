# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root):
        #the result will store the highest path sum found anywhere in the tree
        res = float('-inf')

        #helper dfs function to return the max gain from from the bottom up
        def dfs(node):
            nonlocal res

            #if we reach a null node, return 0 because it adds nothing to the path
            if not node:
                return 0

            #recursively get the max path sum from the left and right children and if a child node has a negative value, drop it by comparing with 0
            leftMax = max(0, dfs(node.left))
            rightMax = max(0, dfs(node.right))

            #the best path including this node as the pivot is the sum of the value of this node along with the nodes along side it
            res = max(res, node.val + leftMax + rightMax)

            #return the best single direction path going upward, either left or right but not both
            return node.val + max(leftMax, rightMax)

        #initial call to adjust values for the result
        dfs(root)

        #return the result after all nodes have been processed
        return res
