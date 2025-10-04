class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1

        if len(nums) <= 1:
            return 0

        while l < r:
            m = (l + r) // 2

            if m+1<len(nums) and nums[m]<nums[m+1]:
                l = m+1
            elif m+1<len(nums) and nums[m]>nums[m+1]:
                r = m
        
        return l