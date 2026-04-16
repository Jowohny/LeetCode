# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        #edge case
        #if the depth of the nodes we need to add is the first level, then create a new node with the given value and set the old tree to the left of the new one
        #return the new tree node
        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot
        
        #create a deque and initialize it with the root
        q = deque([root])

        #use this to keep track of which level we are in the tree, start at level 1
        level = 1

        #loop while there are still loops in the deque
        while q:

            #we want to stop one level before the target depth
            if level == depth-1:

                #the current length of the deque at this given point is the current amount of nodes in this level
                for _ in range(len(q)):

                    #pop off the next node in the deque for processing 
                    node = q.popleft()

                    #create a temporary variable to keep a reference to the left and right nodes
                    tempLNode = node.left
                    tempRNode = node.right

                    #create a new node with the given value and assign it to the current node's left and right
                    node.left = TreeNode(val)
                    node.right = TreeNode(val)

                    #go down the path of the of the newly created nodes and reassign the temporary nodes to the left/right and connect them back to the tree
                    node.left.left = tempLNode
                    node.right.right = tempRNode   

                #seeing how we've gotten to this level already, there is no need to process any further, so just return the new altered root
                return root

            #loop for all the current nodes in this level
            for _ in range(len(q)):

                #pop off the next node in the deque for processing 
                node = q.popleft()

                #if this node has an existing left or right node, then add them to the deque for later processing
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            #increment the current level
            level += 1

        #return the root here if not during the iteration of the tree
        return root