class Solution:
    def commonFactors(self, a: int, b: int) -> int:

        #the amount of common factors for both number can only lie within the range of 1 to the smallest number between a and b
        smaller = min(a,b)

        #keep track of how many common factors there are as we explore the range
        count = 0

        #iterate through the range of 1 to the smaller number
        for i in range(1, smaller+1):

            #if the current number happends to be a multiple of both numbers, add 1 to the total amount of common factor they share
            if a % i == 0 and b % i == 0:
                count += 1
            
        #after testing all numbers in the range of possibiliy, return the total amount of common factors
        return count