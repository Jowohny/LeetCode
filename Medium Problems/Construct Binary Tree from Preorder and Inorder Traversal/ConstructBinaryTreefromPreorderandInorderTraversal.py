# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #create a dictionary with values paired with their index within the inorder list and use an index counter to iterate through the preorder list
        indexDict = {v:i for i,v in enumerate(inorder)}
        curIndex = 0

        #we use the preorder list to define what comes first as well as to find the split in the inorder list to define what goes in which subtree
        #treat each node in the preorder list as its own root
        def build(left, right):
            nonlocal curIndex, indexDict

            #use the overall index to find the value we are processing, increment the index, then create a new node using the found value
            curVal = preorder[curIndex]
            curIndex += 1
            node = TreeNode(curVal)

            #use the found value to find its index within the inorder list through the hashmap
            mid = indexDict[curVal]

            #build onto the left and right subtree until the boundaries overlap, meaning we reached the leaf nodes
            if left <= mid-1:
                node.left = build(left, mid-1)
            if mid+1 <= right:
                node.right = build(mid+1, right)
            
            #this returns the final root node after all recursion is done
            return node

        #return intialized call with the length of the whole list
        return build(0, len(inorder)-1)