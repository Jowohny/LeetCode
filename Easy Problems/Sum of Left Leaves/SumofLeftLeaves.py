# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        #do an initial check to see if the tree exists, it doesn't then return 0 since there's no left leaf
        #initialize a queue with the root along with a variable to keep track of all the left leaf node values
        #if the current node has a left child that is a leaf, add its value to the total sum 
        #if not, add it to the queue to keep checking its children later
        #always add the right child to continue the traversal in case theres a left leaf somewhere else
        #keep looping until the queue is empty, meaning we’ve visited every node
        #return the total sum of all left leaves collected during the traversal

        if not root:
            return 0

        res = 0 
        q = deque([root])
        while q:
            node = q.popleft()
            if node.left:
                if not node.left.left and not node.left.right:
                    res += node.left.val
                else:
                    q.append(node.left)
            if node.right:
                q.append(node.right)
        return res
