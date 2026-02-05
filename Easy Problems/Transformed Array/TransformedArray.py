class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:

        #gotta love the one liner solutions :D
        #if if the current number is 0, then there is no transform that needs to be made
        #when iterating through the original array, unumerate the array to we have the reference index in relation to the value associated at that index
        #for any number that isn't 0, add the value to its index and modular divide it so the new index stays within bounds 
        return [0 if n == 0 else nums[(i+n)%len(nums)] for i,n in enumerate(nums)]