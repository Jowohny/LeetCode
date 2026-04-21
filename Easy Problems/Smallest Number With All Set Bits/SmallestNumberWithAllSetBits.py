class Solution:
    def smallestNumber(self, n: int) -> int:

        #start from the 0th power
        power = 0

        #with numbers with only set bits, they are always 1 less than 2 raised to a certain power
        #only check whether that (2^n)-1 is less than the given number, so that when it is greater, its already the next greatest with set bits
        #doing it this way has a worst case of O(32), pretty much O(1) since 2^32 is the max a number can be
        while True:
            if (2**power)-1 >= n:
                return (2**power)-1
            
            #increment the power
            power += 1