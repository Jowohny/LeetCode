class Solution:
    def numberOfSteps(self, num: int) -> int:

        #use this to keep track of how many operations are needed
        steps = 0

        #continue to loop while the number is greater than 0
        while num > 0:

            #if the right most bit is 1, that means the number is odd, so subract one from the number
            #if the right most bit is 0, then the number is even, so bit shift it to the right by 1, essentially dividing the number by 2
            if num & 1:
                num -= 1
            else:
                num >>= 1

            #increment the amount of steps
            steps += 1

        #return the total amount of steps it took to reduce the number to 0
        return steps
