# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        #keep a resulting list to store all values that are the most frequent
        res = []

        #create a deque and initialize it with the root
        q = deque([root])

        #create a dictionary to keep track of the most frequencies of all elements
        freq = {}

        #keep a overall max value so we know what to keep in the final list
        curMax = float('-inf')

        #keep looping until all node are explored
        while q:

            #pop the node off the front of the deque to get its information
            node = q.popleft()

            #add 1 the the current nodes frequency value in the current dictionary
            freq[node.val] = freq.get(node.val,0) + 1

            #compare the current max to the one found in the dictionary at the current node value
            curMax = max(curMax, freq[node.val])

            #if the current node has any children nodes, the add them to the deque
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        #go through the frequency dictionary and add all values that have a freq equal the to max that was found during node processing
        return [v for v,f in freq.items() if f == curMax]

            
        