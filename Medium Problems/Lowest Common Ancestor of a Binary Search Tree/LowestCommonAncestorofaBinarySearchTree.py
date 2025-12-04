# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #initialize a traversal node with the root
        curNode = root

        #go thorough the levels of the tree until we find the ancestor node
        while curNode:

            #if the value of both nodes are greater than the value of the current node, go down the right path
            #if the value of both nodes are less than the value of the current node, go down the left path
            #if none of those conditions are true, it means that the nodes are in seperate paths from the current node, making the current node common ancestor
            #it could also mean that the current node is the ancestor
            if p.val > curNode.val and q.val > curNode.val:
                curNode = curNode.right
            elif p.val < curNode.val and q.val < curNode.val:
                curNode = curNode.left
            else:
                return curNode