# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        #do an initial check to see if a root exists
        #create a list to add all the max values in each level to
        #intialize a queue with the root to perform BFS
        #for every level, use a max variable to keep track of highest number while going through the nodes
        #add the left and right nodes from the current if they exist to the queue
        #after each level, add the max value to the result array
        #after all nodes have been processed then return the result array
        if not root:
            return []

        res = []
        q = deque([root])
        while q:
            levelMax = float('-inf')
            for _ in range(len(q)):
                node = q.popleft()
                if node.val > levelMax:
                    levelMax = node.val
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(levelMax)
        return res
        