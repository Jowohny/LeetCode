class Solution:
    def checkDivisibility(self, n: int) -> bool:
        #we need to check if n divides evenly by the sum of its digits plus the product of its digits
        #first pull every digit off of n one at a time and stash them in a list
        #add all those digits together to get the digit sum
        #multiply all those digits together to get the digit product
        #n passes if dividing it by (sum + product) leaves no remainder

        digitList = []
        num = n

        #chip off the last digit each loop and shrink num until theres nothing left
        while num > 0:
            digitList.append(num%10)
            num //= 10

        #the sum of the digits
        s = sum(digitList)

        #build up the product of the digits, starting at 1 so the multiplying works
        p = 1
        for d in digitList:
            p *= d

        #n is divisible if it splits cleanly by the digit sum plus the digit product
        return n%(s+p) == 0