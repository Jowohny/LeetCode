class Solution:
    def bitwiseComplement(self, n: int) -> int:

        #create a mask the length of the amount of bits in the given number plus another, then subtract one from it to get a mask of all ones the length of the amount of bits in the given number
        #check if the given number is 0 as it is an edge case, since the bit length of 0 registers as 0, the mask won't work and we have to assign it manually
        mask = (1 << n.bit_length())-1 if n != 0 else 1

        #to find the compliment, use the XOR(^) to compare the bits of the mask and the bits of the number, the bits in the number that are 0 become 1(0^1 = 1), and 1 becomes 0(1^1 = 0)
        return(mask ^ n)