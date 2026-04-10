class Solution:
    def findComplement(self, num: int) -> int:

        #create a mask the length of the amount of bits in the given number plus another, then subtract one from it to get a mask of all ones the length of the amount of bits in the given number
        mask = (1 << num.bit_length())-1

        #to find the compliment, use the XOR(^) to compare the bits of the mask and the bits of the number, the bits in the number that are 0 become 1(0^1 = 1), and 1 becomes 0(1^1 = 0)
        return(mask ^ num)