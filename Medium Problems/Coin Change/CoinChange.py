class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #start from the bottom up, meaning we start from 0 and build up to the amount we are trying to reach
        #create a list initialized with high values with the length of amount+1, since each index represents
        #the minimum number of coins needed to reach that exact amount
        #set the 0th index as 0, because it takes 0 coins to make an amount of 0
        #for every index from 1 to amount, go through each coin and check if we can subtract that coin from the current amount 
        #if we can, update list at the current index with the minimum between its current value and the value we've memoized in the list at the index of difference 
        #the further we go, the more memoized the list becomes, since each cost up to that point depends on previous values that we have already solved before
        #if the value given at the amount index hasnt changed from the start, then that means that there was no combination of coins to make up the amount
        #otherwise, return the value at the index
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-c])

        if dp[amount] != float('inf'):
            return dp[amount]
        else:
            return -1
