# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        #reference the root of the tree to iterate through
        current = root

        #only loop while the current iterated node is a valid one
        while current:

            #if the current node has a left node, store the left subtree in a temporary variable
            #in that left subtree, traverse to the furthest right node
            #attach all nodes found to the right of the current node to the furthest right node found in the left subtree
            #copy everything over from the current left subtree all to the right and set the old left subtree to none
            if current.left:
                temp = current.left
                while temp.right:
                    temp = temp.right
                temp.right = current.right
                current.right = current.left
                current.left = None

            #iterate down the right subtree to seek out any nodes that have a potential left subtree
            current = current.right    
        