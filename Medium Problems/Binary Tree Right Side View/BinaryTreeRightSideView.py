# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
				#if there isnt a root, return a blank list as there is no right view on a None
        if not root:
            return []

				#initialize a deque with the root of the tree along with a result list to store far right nodes
        q = deque([root])
        res = []

				#continue while there are still items within the queue
        while q:

						#store the length of the q so when we want to access it later it doesn't change when we pop for the value
            l = len(q)
            for i in range(l):

								#pop node in front for its information
                node = q.popleft()

								#if the node is at the end of the current level, add it to the result list
                if i == l - 1:
                    res.append(node.val)

								#if the left or right node exist, add then to the list for later processing
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
				#return the result after all nodes have been processed
        return res
