# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #use BFS and queue to iterate through every node in the tree
        #start off by adding the root in the queue
        #add left and right nodes of the nodes at the front of the queue
        #for every node we traverse within the tree, we add a level to the current total
        #we continue this until the queue is empty, meaning we have explored every node

        q = deque()
        if root:
            q.append(root)

        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level