# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        #initialize a variable to keep track of the value of the node visited before the current one
        prev = None

        #set the result to infinity so that the first difference found will always be smaller
        res = float('inf')
        
        def inorder(node):
            nonlocal prev, res

            #go far down the left side first to have access to the smallest values
            if node.left:
                inorder(node.left)
            
            #process the current node after finishing its entire left subtree
            #if this isn't the very first node we've visited, calculate the gap between it and the previous node
            if prev is not None:

                #update the global minimum if the current gap is smaller then out global minimum
                if node.val - prev < res:
                    res = node.val - prev
            
            #update the previous ndoe marker to the current node's value before moving to the right
            prev = node.val
            
            #traverse the right side to visit the larger values in the subtree
            if node.right:
                inorder(node.right)
            
        #start the traversal at the root
        inorder(root)
        
        #return the smallest difference found across all of the tree nodes
        return res