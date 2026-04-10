class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        #start with 1 since the 0th power of 4 is 1
        currPower = 1

        #loop while the current power value is less than n
        while currPower <= n:

            #return true if the current power is n
            if currPower == n:
                return True

            #keep bitshifting to the left twice to add a power of 4
            currPower = currPower << 2

        #if the current power is found to be over n, then n isn't a power of 4
        return False
        