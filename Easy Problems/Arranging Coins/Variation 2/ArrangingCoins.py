class Solution:
    def arrangeCoins(self, n: int) -> int:
        #use binary search to look for the most amount of rows the current amount of coins can create
        #find the mid point and and use it to calculate how many coin you need to fill that amount of rows
        #if the amount of needed coins is less than the amount given, move left pointer to find higher row count
        #if the amount of needed coins is higher than the amount given, move right pointer to find lower row count
        #return the right pointer as it holds the higher amount of rows
        
        l, r = 1, n
        
        while l <= r:
            m = (r + l) // 2
            coins = (m * (m + 1)) // 2
            
            if coins <= n:
                l = m + 1
            else:
                r = m - 1
                
        return r