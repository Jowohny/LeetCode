class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #2 pointers
        #we need to check if the element after if lower than the first, otherwise we can't profit
        #if the number is lower than the next, we check how much profit can be made
        #we keep going until we find another number smaller and we continue checking

        left, right = 0, 1
        maxProfit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right
            right += 1
        return maxProfit
