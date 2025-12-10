# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        #append all values of the tree into a list
        res = []

        def dfs(node):
            nonlocal res

            #if the current node is null, then add to the list as null
            if not node:
                res.append('null')
                return
            
            #if the current node as a value, then stringify it and add it to the list
            res.append(str(node.val))

            #go down each substree, make the list return the outcome of a preorder traversal
            dfs(node.left)
            dfs(node.right)

        #initial dfs call on the root
        dfs(root)

        #combine list into one string and seperate each value with a comma for convenient deserialization
        return ','.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        #split the data into a list off of the commas and use index to keep track of where we are on the tree
        dataList = data.split(',')
        index = 0

        def dfs():
            nonlocal dataList, index

            #if the value of the current index in the data list is null, then no node exists there, so reture None and increase the index
            if dataList[index] == 'null':
                index += 1
                return None

            #create a new node with the integer converted value found from the index in the data list, then increase the index
            node = TreeNode(int(dataList[index]))
            index += 1

            #for each of the subtrees, go down each path, the tree gets printed the with the closest nodes to the root first, or preorder
            node.left = dfs()
            node.right = dfs()

            #return the node to fill in the tree
            return node

        #initial dfs call
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))