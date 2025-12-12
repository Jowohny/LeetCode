class Solution:
    def numSquares(self, n: int) -> int:
        #create a dp array to dynamically fill in as we go up to n
        dp = [0] + [float('inf')]*n

        #fill an array with the complete squares up to n if the square is less than n
        squares = [i*i for i in range(1,n+1) if i*i <= n]

        #use this loop to fill in the dp array from 1 - n
        for i in range(1,n+1):

            #test all in the possible range, use the difference to find if the amount has already been found
            for s in squares:

                #the current square is less than the index, repesenting its own spot on the dp array
                #if there was a value difference index found in the dp array, add 1 to its amount to represent the needed additional square to make up its value, otherwise keep the lowest found needed amount
                if i-s >= 0:
                    dp[i] = min(dp[i], 1+dp[i-s])
            
        #return the amount needed at the nth index
        return dp[n]
