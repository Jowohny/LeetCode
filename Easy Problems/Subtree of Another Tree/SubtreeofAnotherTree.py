 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #create a helper method to check if the subTree is the same as the subRoot
        #if there isn't a subroot, then technically nothing already exists in the root
        #if there's no root, then there no subtree to check
        #run the root through the sametree check
        #if that doesn't come out to be true, then call the main method again with the different sub tree as the input parameters
        #if it happens there the root becomes None before it finds a match from either side of the tree, then there is no subtree match

        if not subRoot: return True
        if not root: return False

        if self.sameTree(root,subRoot):
            return True
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return self.sameTree(root.left,subRoot.left) and self.sameTree(root.right,subRoot.right)
        return False