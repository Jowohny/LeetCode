# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #we initialize a result to keep track of how many good nodes we found
        #we also initialize a queue with root along with the value we consider the maximum to be passed with it
        #while there are items in the queue, pop the leftmost item and unpack it
        #if the current node is greater then the maximum found along the way to that node, then it is considered good and we add to the result and set the new maximum
        #add the left and right nodes to the queue if they exists
        #if theres nothing left in the queue, that means we have processed all the nodes
        #return the result which should indicate how many good nodes there were in the tree

        res = 0
        q = deque([(root,float('-inf'))])
        
        while q:
            node,maximum = q.popleft()

            if node.val >= maximum:
                res += 1
                maximum = node.val
            
            if node.left:
                q.append((node.left,maximum))

            if node.right:
                q.append((node.right,maximum))
        return res