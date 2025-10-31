# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        #use a queue to perform BFS to traverse through the tree
        #initialize the queue with the root of the tree
        #keep a variable to keep how many nodes there are in the level and another to track the current sum
        #if the node has any children, add them to the queue
        #once the nodes for each level is done processing, find the average by dividing the current sum and the amoount of nodes in the level
        #when the queue is empty, that is when we processed all nodes, and we return all the averages in the result list
        res = []

        q = deque([root])
        while q:
            divisor = len(q)
            currSum = 0
            for _ in range(divisor):
                node = q.popleft()

                currSum += node.val
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(currSum/divisor)

        return res
                
