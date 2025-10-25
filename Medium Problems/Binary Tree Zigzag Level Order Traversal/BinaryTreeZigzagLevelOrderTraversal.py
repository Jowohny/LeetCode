# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #check for the inital case where there could or could not be a root
        #use a queue initialized with the root to implement BFS to traverse through the tree
        #create a new list for each level to add all nodes within the level
        #if it is an even layer, we read the level from left to right, which means we just add the level to the result list as it is
        #if it is an odd layer, we read the level from right to left, which means we reverse the list for the current level before adding it to the result list
        #once all nodes have been processed, return the result list
        if not root:
            return []

        res = []
        q = deque([root])
        reverse = 0
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if reverse%2==1:
                level = level[::-1]
            res.append(level)
            reverse += 1
        return res