class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #sort the candidates so we can skip duplicates
        candidates.sort()

        def backtrack(index, curSum, remaining):
            #if remaining hits 0, add a copy of the current combination
            if remaining == 0:
                res.append(curSum.copy())
                return

            #initialize the first previous as a negative as we havent found any value yet
            prev = -1
            for i in range(index, len(candidates)):

                #skip duplicate values at the same index level
                if candidates[i] == prev:
                    continue
                prev = candidates[i]

                #stop early if the candidate exceeds the remaining
                if candidates[i] > remaining:
                    break

                #add the current candidate to the current sum
                curSum.append(candidates[i])

                #recall the method increasing index since we aren't allowed to use the same number and take away the current candidate from the remaining
                backtrack(i + 1, curSum, remaining - candidates[i])

                #undo the choice so we have the chance to test all cases
                curSum.pop()

        #instantiated result list and initial method call
        res = []
        backtrack(0, [], target)

        #return resulting list
        return res
