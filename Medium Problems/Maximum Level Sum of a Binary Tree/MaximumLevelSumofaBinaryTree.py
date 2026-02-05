python 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        #keep a global max we as process all the nodes within the tree
        gMax = float('-inf')

        #use a variable to store the level with the greatest sum
        res = 0

        #use another variable to keep track of the level we are on
        currLevel = 1

        #create a queue and initialize it with the root of the tree
        q = deque([root])

        #loop until all tree nodes are processed
        while q:

            #keep track of the sum of all node in the current level
            currSum = 0

            #loop for every node in this level
            for _ in range(len(q)):

                #get the next node to be processed from the queue
                node = q.popleft()
                
                #add the current value of the node to the level sum tracker
                currSum += node.val

                #if the current node has any child nodes, add them to the queue to be processed later
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            #if the sum of the current level is the greatest we have seen so far, then record the level and replace the previous max
            if currSum > gMax:
                res = currLevel
                gMax = currSum
            
            #increment the level to indicate our process through the tree
            currLevel += 1

        #after processing all the nodes, return the level with the greatest sum in the tree
        return res