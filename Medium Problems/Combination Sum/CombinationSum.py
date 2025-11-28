class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        #create a backtracking method with an index, so we never go backwards in the list to avoid duplicates, the current list of numbers to reach the target, and the remaining left after subtracting a value from the target
        def backtrack(index,curSum,remaining):

            #cycle through all the candidates within the list
            for i in range(index, len(candidates)):

                #do an initial check on whether the current candidate is less than or equal to the remaining left
                #add the current candidate to the running list if found to be less than or equal to
                #after every addition, we also need to pop the same values after use to test other combinations
                if candidates[i] < remaining:
                    curSum.append(candidates[i])

                    #continue to backtrack if we still have more remaining
                    backtrack(i, curSum, remaining-candidates[i])
                    curSum.pop()
                elif candidates[i] == remaining:
                    curSum.append(candidates[i])

                    #if the candidate is exactly the same number as the remaining, add it to the running list and return a copy of it, not a reference
                    res.append(curSum.copy())
                    curSum.pop()
        
        #initial call and instantiated result list
        res = []
        backtrack(0,[],target)
    
        #return result list after method call
        return res
