class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        #the minimum size the list could be 2 since the most duplicates allowed are 2
        #at a list size 2, either both numbers are the same or they are both different, which fit the requirements
        k = 2

        #start at 2 since we know any list size 2 or less is already right
        for i in range(2, len(nums)):

            #since the list is sorted, the same numbers are grouped together
            #if this condition doesn't pass, then that means there was a third repeating element, otherwise, it is a valid element to be replaced in the array
            #replace the index corresponding to the resulting list size(k) with the current index
            #increment the 'what should be' size of the list(k)
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1

        #this represents the part of the array that should meet the requirements
        return k