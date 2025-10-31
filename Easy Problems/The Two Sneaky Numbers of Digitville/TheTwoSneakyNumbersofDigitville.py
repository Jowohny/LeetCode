class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        #create a set to check for duplicates
        #add duplicates to a result array
        #run through all nums in the list
        #return the result
        res = []
        numset = set()
        for n in nums:
            if n in numset:
                res.append(n)
            else:
                numset.add(n)

        return res