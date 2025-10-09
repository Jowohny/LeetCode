class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #do a basic binary search  in which you are trying to find an element, except you approach 
        #a point in which the pointers overlap, and when they do, the left pointer falls upon the 
        #insertion point

        l, r = 0,len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return l