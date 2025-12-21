class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #initialize the left and right pointers that represent the range in which we are searching
        l,r = 0,len(nums)-1

        #loop until the left and right pointers overlap
        while l <= r:

            #get the midpoint of the current range
            m = (l+r)//2

            #if the value of the middle index in the list is equal to our target, return the index
            #if the the value of the middle index is less than the target, move the left pointer to the middle index to decrease the range of the search
            #if the the value of the middle index is greater than the target, move the right pointer to the middle index to decrease the range of the search
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        #if the pointers have overlapped and no index was returned, that means the target wasn't in the list
        return -1