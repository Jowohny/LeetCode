class Solution:
    def addDigits(self, num: int) -> int:
        #variable to store single digit for the result
        res = num

        #loop until we have a number that is less than 10, or just a singular digit
        while num >= 10:

            #reset the storage variable to compute the next digit sum
            res = 0

            #loop until all the numbers in the current number variation is added together
            while num > 0:
                res += num % 10
                num //= 10

            #set the number to the sum of the digits
            num = res        

        #when the number becomes a single digit, return the number
        return res