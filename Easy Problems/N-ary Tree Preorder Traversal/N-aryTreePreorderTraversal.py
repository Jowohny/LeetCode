"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        #create a DFS function to traverse through the tree
        #append the current value to the tree and go through the child nodes from left to right
    
        res = []
        
        def dfs(node: Optional['node']) -> None:
            if not node:
                return
            
            res.append(node.val)
        
            for i in node.children:
                dfs(i)

        dfs(root)
        return res 
