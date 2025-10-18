# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #we use DFS to go all the way down each branch and get the height of each subtree
        #for each node, check if both sides are balanced and that their heights differ by no more than 1
        #if any subtree fails that condition, its unbalanced
        #return True if the tree is balanced, otherwise False

        def dfs(node):
            if not node:
                return [True, 0]

            l = dfs(node.left)
            r = dfs(node.right)
            if l[0] and r[0] and abs(l[1] - r[1]) <= 1:
                return [True, 1 + max(l[1], r[1])]
            else: 
                return [False, 1 + max(l[1], r[1])]

        return dfs(root)[0]