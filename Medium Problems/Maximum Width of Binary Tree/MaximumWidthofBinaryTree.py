# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root):
        #keep a comparator to keep the max with of each level going through the tree
        maxWidth = float('-inf')

        #initalize a deque with the root and a 0 index since the root is the start
        q = deque([(root, 0)])

        #keep running until all node have been processed
        while q:
            
            #get the current length of the level and store it so we dont get a different value referencing later
            curLen = len(q)

            #get the index of the first node that appears in the level
            first = q[0][1]

            #run for the amount of nodes found in the queue after each iteration
            for i in range(curLen):

                #pop the first node off the queue and unpack it into its node and its index within the level
                node, index = q.popleft()

                #make the index start at 0 to avoid large number computation later into the tree
                index -= first

                #at the end of the current level, compare the current index and the current max width
                if i == curLen - 1:
                    maxWidth = max(maxWidth, index + 1)

                #if the current node has any child nodes, add them to the queue and increase the index accordingly
                if node.left:
                    q.append((node.left, 2 * index))
                if node.right:
                    q.append((node.right, 2 * index + 1))

        #after all nodes have been processed, return the level with the max width
        return maxWidth
