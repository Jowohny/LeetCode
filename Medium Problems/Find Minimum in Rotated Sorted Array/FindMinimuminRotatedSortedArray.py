class Solution:
    def findMin(self, nums: List[int]) -> int:
        #use modified binary search to apply to rotated array
        #set up variable to keep track of minimum value
        #considering the array will be most likely rotated, some elements will be in order and others will be out of order
        #check both values the index of the pointers to see if they are sorted
        #if they are, take the minimum value and break out of the loop, by then the algorithm would have zoned in the the absolute minimum
        #if not continue to the other conditions
        #find the middle value and take the current minimum
        #check where the middle value is in comparison to the pointers
        #if a section of the array if found to be sorted, we explore the other side to find the minimum
        #at any point, if the left pointer value is greater than the right pointer value, then the current section is unsorted
        #return the minimum when the section between part left and right pointer are in order 
        #also return the minimum after running through the entire loop 
        l,r = 0,len(nums)-1
        minimum = float('inf')

        while l <= r:
            if nums[l] < nums[r]:
                return min(minimum, nums[l])
            
            m = (l + r)//2
            minimum = min(minimum, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        return minimum