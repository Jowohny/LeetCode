class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        #sort the list so its easier to skip any duplicates
        nums.sort()

        #keep track of how many unique pairs there are
        total = 0

        #initialize 2 pointers
        l, r = 0, 1
        while r < len(nums):

            #make sure that l and r don't overlap
            if l == r:
                r += 1
                continue

            #check if both pointers are in bounds before computing
            if l >= len(nums) or r >= len(nums):
                break 

            #calculate the difference between the 2 pointers value
            diff = nums[r] - nums[l]

            #if the current pointer difference is smaller than k, move the right pointer
            if diff < k:
                r += 1
            
            #if the current pointer difference is larger then k, move the left pointer
            elif diff > k:
                l += 1
            
            #if the current pointer difference is equal to k, then add 1 to the total and move both pointers
            else:
                #if the 
                total += 1
                l += 1
                r += 1

                #skip duplicate numbers so we have only unique pairs
                while l < len(nums) and nums[l] == nums[l-1]:
                    l += 1

        #return the total pairs found after the right pointer goes out of bounds
        return total
