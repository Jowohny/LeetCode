class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        #use a variable to to keep track of how many operations as we check through the loop
        #whenever you are in between 2 numbers are divisible by 3 (i.e. 0 -> 1,2 -> 3), you are always one operation away from making the current number dvisible by 3
        #all we need to do is to check whether the number is or is not divisible by 3 and add to the total amount of operations
        #after we go through the whole loop, return the amount of operations
        ops = 0

        for i in nums:
            if i%3 != 0:
                ops += 1
        
        return ops