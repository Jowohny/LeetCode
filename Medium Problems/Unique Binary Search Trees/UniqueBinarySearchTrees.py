class Solution:
    def numTrees(self, n: int) -> int:
        #every value from 1 to n can take a turn being the root of the tree
        #whatever number is the root, the smaller values go left and the larger values go right
        #so the count for a root is the ways to build the left subtree times the ways to build the right subtree
        #the number of unique trees only depends on how many nodes there are, not which exact values they hold
        #build up a dp table where dp[i] is the number of unique trees you can make with i nodes

        #there is exactly one empty tree and one single node tree
        dp = [0] * (n + 1)
        dp[0] = 1
        if n >= 1:
            dp[1] = 1

        #fill the table for every tree size from 2 up to n
        for nodes in range(2, n + 1):

            #try each position as the root, splitting the rest into a left and right side
            for root in range(1, nodes + 1):

                #root-1 nodes fall to the left, the remaining nodes fall to the right
                dp[nodes] += dp[root - 1] * dp[nodes - root]

        return dp[n]
