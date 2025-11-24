class Solution:
    def averageValue(self, nums: List[int]) -> int:
        #keep a variable to tally up how many numbers and the sum of said numbers in the list are even and divisible by 3
        #the lowest common denominator is 6 we can just find numbers that are divisible by 6 and add them to the sum and tally
        #to avoid division by 0 error, check of there were any numbers that were found
        #return the average using the sum and the total and convert to an integer

        sumAve = 0
        totalAve = 0
        for n in nums:
            if n % 6 == 0:
                sumAve += n
                totalAve += 1
        
        if totalAve == 0:
            return 0

        return int(sumAve/totalAve)