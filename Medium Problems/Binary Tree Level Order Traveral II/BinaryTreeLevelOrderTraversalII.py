# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        #use bfs to traverse the tree level by level starting from the root
        #keep a queue to process nodes in the current level before moving to the next
        #for each level, pop all nodes from the queue and store their values in the list for the curret level
        #append left and right children of each node to the queue for the next level processing
        #after finishing a level, add all its values to the result list
        #once all levels are processed, reverse the result list
        #return the reversed list of levels

        res = []
        q = deque([root])
    
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
        return res[::-1]