# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #check if the root is None, if so return None since there is no tree to invert
        #use a deque instead of a list for faster append and pop operations
        #initialize the deque with the root node
        #use a while loop to go through all nodes until the deque is empty
        #pop the last node from the deque to process it
        #swap the left and right children of the current node
        #if the left child exists after swapping, add it to the deque to process later
        #if the right child exists after swapping, add it as well
        #continue until all nodes have been swapped and the deque is empty
        #return the root node which now represents the fully inverted tree

        if root is None:
            return None
        stack = deque([root])
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left: 
                stack.append(node.left)
            if node.right: 
                stack.append(node.right)
        return root

