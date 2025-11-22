class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #have a variable to keep track of the most consecutive ones and another to dynamically track the number of current 1s streak 
        #if the current number is 1, increment the current consecutive 1 counter
        #otherwise, reset the counter
        #after every iteration, check whether the current consecutive count is greater than the most recorded consective count
        #after all list items have been checked, return the most consecutive ones

        most1 = 0
        current1 = 0

        for i in nums:
            if i == 1:
                current1 += 1
            else:
                current1 = 0

            if current1 > most1:
                most1 = current1

        return most1