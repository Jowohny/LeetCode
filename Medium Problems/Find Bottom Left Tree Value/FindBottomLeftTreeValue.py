# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        #create a queue initialized with the root to perform BFS
        #create a list for each level and append all node values per level
        #for every node, check if they have left and right nodes and add them to the queue accordingly
        #until we reach the last layer and all nodes have been explored do we exit the loop and return the first item in the latest level

        q = deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return level[0]


            