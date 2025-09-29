class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        #sort the array so its easy to incriment/decrement based on current total
        #in order to avoid duplicate answers, incriment passed repeating numbers
        #if the current total is less than, incriment, otherwise, decrement
        #if the total numbers equal to 0, add to the result list
        
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            j,k = i+1,len(nums)-1
            while j<k:
                if nums[i]+nums[j]+nums[k] == 0:
                    result.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while nums[j] == nums[j-1] and j<k:
                        j+=1
                elif nums[i]+nums[j]+nums[k] > 0:
                    k-=1
                elif nums[i]+nums[j]+nums[k] < 0:
                    j+=1
        return result