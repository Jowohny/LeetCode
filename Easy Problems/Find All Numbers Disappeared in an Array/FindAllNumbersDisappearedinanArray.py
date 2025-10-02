class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #create a set that initializes numbers from 1 to then length of the list
        #put the current nums list into a set to get rid of duplicates
        #subtract set to get non intercepted numbers
        #convert to list format
        return list(set(range(1, len(nums) + 1)) - set(nums))