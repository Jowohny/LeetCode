# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        #use a hashmap to store any values to be later accessed
        hashmap = {}

        #initialize a deque with the root of a tree
        q = deque([root])

        #process all nodes in the tree
        while q:

            #pop the next node in the queue
            node = q.popleft()

            #if the difference of the target value and the current node value is found in the hashmap, then there are 2 node values in the tree that can make up the target sum
            if k - node.val in hashmap:
                return True
            
            #add the current nodes value to the hashmap for later possible referencing
            hashmap[node.val] = 1

            #add left and or right node if they exist
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        #after all nodes have been processed and no nodes have been found to make up the sum of the target, return false
        return False