"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        #use DFS to traverse through the list
        #travel through all nodes and only after all nodes have been visited, append the value to the result and backtrack from there 
        res = []

        def dfs(node: Optional['root']) -> None:
            if not node: 
                return

            for i in node.children:
                dfs(i)

            res.append(node.val)

        dfs(root)
        return res