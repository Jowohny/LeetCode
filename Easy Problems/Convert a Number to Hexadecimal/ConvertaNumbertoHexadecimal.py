class Solution:
    def toHex(self, num: int) -> str:

        #create a string to reference for each value of hex
        hexString = '0123456789abcdef'

        #create a list to add the hex values into
        hexRes = []

        #edge case
        #if the number is 0, just return '0'
        if num == 0:
            return '0'

        #if the number is less than 0, add the upper limit (2**32) to the current number to have a somewhat reversed hex (-1 == 2**32-1, -2 == 2**32-2, etc...)
        if num < 0:
            num += 2**32

        #loop while the number hasn't become 0
        while num:

            #add the next value of the hex into the resulting hex list
            #modular divide the current number by 16(hexa) and use the hex string to get the corresponding hex value
            hexRes.append(hexString[num%16])

            #divide the current number by 16 to get the next value of hex later
            num //= 16

        #by creating the hex from the number down to 0, we must reverse the list before joining the hex values together
        return ''.join(hexRes[::-1])