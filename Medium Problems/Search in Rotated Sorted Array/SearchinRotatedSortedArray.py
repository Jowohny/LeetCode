class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #use modified binary search to search through rotated value
        #check for which 'sorted' section contains the range to check for the target value
        #set that section to the designated pointers
        #perform basic binary search for the target

        l,r = 0,len(nums)-1

        while l <= r:
            m = (l + r)//2
            if target == nums[m]:
                return m

            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1