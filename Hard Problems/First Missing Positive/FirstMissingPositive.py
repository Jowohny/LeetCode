class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #the answer has to be somewhere between 1 and the length of the array plus 1
        #anything outside that range (negatives, zeros, huge numbers) cant be the first missing positive
        #use the array itself as the storage, put each number n at index n-1 where it belongs
        #keep swapping numbers into their correct spot until the current one is out of range or already placed
        #then walk the array, the first index that doesnt hold its matching number reveals the missing positive

        n = len(nums)

        for i in range(n):

            #swap the current number into its correct index as long as it belongs in range and isnt already there
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct = nums[i] - 1
                nums[i], nums[correct] = nums[correct], nums[i]

        #the first slot missing its matching value (index i should hold i+1) is the answer
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        #every slot from 1 to n was filled, so the missing positive is the next one up
        return n + 1
