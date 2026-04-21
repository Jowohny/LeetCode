class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:

        #use this to record how many bits are needed to shift
        result = 0

        #using the XOR operator on the 2 numbers tell us which bits are different at each bit, if they are the same, the bit is 0, if they are different that bit becomes 1
        diff = start ^ goal

        #only continue to loop if the value of diff is not 0
        while diff != 0:

            #if the first bit is 1, meaning that the values at this bit were different for both numbers, add 1 to the result
            if diff & 1:
                result += 1

            #shift the value of the diff over to the right by 1 so we can check the next bit
            diff >>= 1

        #return the amount of bits that are needed to convert the starting number to the goal
        return result