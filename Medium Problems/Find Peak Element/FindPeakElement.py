class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
				#use binary search
				#check if the middle boundary is within the length of the nums
				#also check if the preceeding/proceeding numbers are decreasing/increasing
				#when the pointers overlap, return the left or right pointer as they should be at the peak


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