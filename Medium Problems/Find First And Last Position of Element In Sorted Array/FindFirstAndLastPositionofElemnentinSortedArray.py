class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        iL = -1
        while l <= r:
            m = (l + r) // 2

            if nums[m] >= target:
                r = m - 1
            else:
                l = m + 1
            if nums[m] == target:
                iL = m
        
    
        l, r = 0, len(nums) - 1
        iR = -1

        while l <= r:
            m = (l + r) // 2

            if nums[m] <= target:
                l = m + 1
            else:
                r = m - 1
            if nums[m] == target:
                iR = m
            
        return [iL, iR]