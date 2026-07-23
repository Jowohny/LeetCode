class Solution:
    def myPow(self, x: float, n: int) -> float:
        #use fast exponentiation to avoid multiplying x by itself n times
        #if the exponent is negative, flip x to its reciprocal and make the exponent positive
        #square x each step and halve the exponent
        #whenever the current exponent is odd, multiply that squared value into the running result
        #keep going until the exponent reaches 0, the running result is the answer

        if n < 0:
            x = 1 / x
            n = -n

        res = 1

        while n > 0:

            #if the current exponent is odd, fold the current value of x into the result
            if n % 2 == 1:
                res *= x

            #square x and halve the exponent for the next step
            x *= x
            n //= 2

        return res
