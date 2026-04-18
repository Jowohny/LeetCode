.# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        #create a deque and initialize it with the root
        q = deque([root])

        #use this to keep track of what level we are on
        level = 0 

        #only loop while there are nodes left in the deque
        while q:

            #if the current level is odd, start reversing the level by swapping the edges and repeat going inward
            if level%2 == 1:

                #only loop for around half the length of the deque since thats all we need
                for i in range(len(q)//2):
                    s,e = q[i], q[-(i+1)]
                    s.val, e.val = e.val, s.val

            #loop for all the nodes currently in this level
            for _ in range(len(q)):

                #pop off the next node in the deque for processing 
                node = q.popleft()

                #if this node has an existing left or right node, then add them to the deque for later processing
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            #increment the level
            level += 1

        #return the root after all the nodes in the odd levels have been reversed
        return root