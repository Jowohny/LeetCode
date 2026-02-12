class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        #get all distinct numbers by slamming the numbers into a set
        nums = set(nums)

        #if the amount of all unique numbers in the list is less than 3, take the max of the list, since there can't be a third maximum number
        if len(nums) < 3:
            return max(nums)

        #if the amount of all unique numbers in the list is more than 3, sort the list and take the 3 to last number in the sorted list
        else:
            return sorted(nums)[-3]