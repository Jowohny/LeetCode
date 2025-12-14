class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        #keep a list for the current round of integers to be added in
        curr = []
        eo = True
        #run until there is only 1 integer remaining
        while len(nums) > 1:

            #skip 2 indexes at a time to compare each unique index value
            for r in range(0,len(nums),2):

                #alternate between min and max when comparing pairs 
                if eo:
                    curr.append(min(nums[r],nums[r+1]))
                else:            
                    curr.append(max(nums[r],nums[r+1]))
                
                eo = not eo

            #set the current round to process the next round
            nums = curr

            #reset current round for next rounds values
            curr = []
        
        #return the only left number in the list
        return nums[0]
        
            
