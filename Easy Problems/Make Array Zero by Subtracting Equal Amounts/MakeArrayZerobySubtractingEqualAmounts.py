class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        #grab all the numbers from the nums list that are not 0 and then put it into a set
        newList = set([n for n in nums if n != 0])

        #return the length of the set as the amount of different numbers there are defines the amount of operations
        return len(newList)