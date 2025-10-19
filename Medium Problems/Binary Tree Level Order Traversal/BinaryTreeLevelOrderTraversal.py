# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #use BFS to add all neighbors of nodes from the current level
        #the nodes added represent the nodes on the next level
        #create a separate list isntance for each level and add to the result array after the value of each node in the level is added
        #if the length of the list is 0, don't add anything

        q = deque([root])
        res = []

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if len(level) > 0:
                res.append(level)
        return res 
