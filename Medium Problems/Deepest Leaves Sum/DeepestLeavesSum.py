# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        #create a deque and initialize it with root
        q = deque([root])

        #use this to keep track of each level total value
        currSum = 0

        #loop while there are nodes still in the queue
        while q: 

            #reset the previous level's sum to replace it with this level's sum
            #since there were more nodes to process, the last level couldn't have been the deepest leaves
            currSum = 0

            #loop for all the nodes currently in this level
            for _ in range(len(q)):

                #pop off the next node in the deque for processing 
                node = q.popleft()

                #add the node of the current node to the current sum of the level
                currSum += node.val

                #if this node has an existing left or right node, then add them to the deque for later processing
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        #return the sum of the deepest leaves, or just the sum of the nodes on the last level
        return currSum