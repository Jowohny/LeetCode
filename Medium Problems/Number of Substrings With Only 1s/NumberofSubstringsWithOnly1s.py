class Solution:
    def numSub(self, s: str) -> int:
        #initialize a counter to track how many consecutive 1s we have seen so far and a total variable to store the total number of valid substrings formed from all runs of 1s
        #when we see a 1, increase the consecutive counter because the more consecutive 1s there are, the more substrings there are
        #add the current consecutive count to the total since every new 1 creates more substrings
        #when we see a 0, reset the counter because there are no more consecutive 1s
        #return the total count of all substrings made 
        count = 0
        total = 0

        for c in s:
            if c == '1':
                count += 1
                total += count
            else:
                count = 0

        return total % ((10**9) + 7)
