# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        #the array is sorted, so the middle element makes a balanced root
        #everything left of the middle is smaller and becomes the left subtree
        #everything right of the middle is larger and becomes the right subtree
        #recurse on each half to build those subtrees the same way
        #picking the middle every time keeps the height balanced

        #helper that builds a balanced tree from the slice between l and r
        def build(l, r):

            #if the left index passes the right, this branch is empty
            if l > r:
                return None

            #grab the middle of the current slice to use as the root
            mid = (l + r) // 2
            node = TreeNode(nums[mid])

            #build the left subtree from the values before the middle
            node.left = build(l, mid - 1)

            #build the right subtree from the values after the middle
            node.right = build(mid + 1, r)

            return node

        return build(0, len(nums) - 1)
