class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        #add all the numbers in the list together and then mod it by the given k and return it
        res = 0

        for n in nums:
            res += n

        return res%k