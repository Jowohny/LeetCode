class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #sort the list so its eaiser to skip duplicates
        nums.sort()

        def backtrack(index, currSet):
            #store a copy of the current subset instead of the reference
            res.append(currSet.copy())

            for i in range(index, len(nums)):
                #skip duplicates so we don't build the same subset twice
                if i > index and nums[i] == nums[i-1]:
                    continue

                #add the current number from the index value in nums to the current variation of this subset
                currSet.append(nums[i])

                #recall the method with an increase in the index along with the updated subset
                backtrack(i+1, currSet)

                #pop the latest value from the current subset so we can get all possibilities
                currSet.pop()
        
        #instantiate the result list and initial backtrack call
        res = []
        backtrack(0, [])

        #return the resulting list
        return res
