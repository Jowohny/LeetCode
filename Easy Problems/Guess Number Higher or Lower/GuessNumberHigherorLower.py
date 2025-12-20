# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        #intialize the pointers that create the range for our binary search
        l,r = 1,n

        #loop until the pointers overlap each other
        while l <= r:

            #calculate the current midpoint using the pointers
            m = (l+r)//2

            #use the predefined guess method to get an input
            #if 0 is returned, then we guessed correct 
            #if 1 is returned, then we guessed too high, meaning we need to bring the search range to the current first half
            #if -1 is returned, then we guessed too low, meaning we need to bring the search range to the current second half
            if guess(m) == 0:
                return m
            elif guess(m) == 1:
                l = m + 1
            else:
                r = m - 1

        #if the number is somehow not found in the loop, then return -1 meaning we couldn't guess it
        return -1