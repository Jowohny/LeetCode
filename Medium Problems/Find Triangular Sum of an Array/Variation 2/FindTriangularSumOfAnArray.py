class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        #if length of nums list is equal to 1, return the current num list
        #add value at index i along with then next value and go through the list
        #after each iteration, decrement list size by one and replace current list with the newer one

        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return (nums[0] + nums[1]) % 10

        currList = nums

        while len(currList) > 1:
            for i in range(len(currList)-1):
                currList[i] = (currList[i] + currList[i+1])%10
            currList.pop()

        return currList[0]

            