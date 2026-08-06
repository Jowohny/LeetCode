class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        #we want the smallest number that is at least n whose digits multiply into something divisible by t
        #the numbers are small, so just start at n and walk upward one at a time
        #for each candidate, multiply all of its digits together to get the digit product
        #if that product divides evenly by t, this is the first number that works
        #keep climbing until we find one, an answer is always within a short reach of n

        num = n

        while True:

            #multiply every digit of the current number together
            product = 1
            for ch in str(num):
                product *= int(ch)

            #the first number whose digit product is divisible by t is our answer
            if product % t == 0:
                return num

            #this one didnt work, try the next number up
            num += 1
