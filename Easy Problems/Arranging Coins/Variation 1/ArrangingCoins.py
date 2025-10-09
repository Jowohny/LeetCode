class Solution:
    def arrangeCoins(self, n: int) -> int:
        #use a while to run while the n is still greater than the current index
        #subtract the current index from n
        #increment the index(row count) until n is less than the current index

        i = 0
        while n > i:
            i += 1
            n -= i
        return i