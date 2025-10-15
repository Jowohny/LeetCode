class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        #use backtracking to generate all possible permutations from the given list
        #keep a set to track unique permutations and avoid adding duplicates to the result
        #initialize a result list to store all valid permutations
        #make a recursive function to create permutations
        #if the current index has reached the end of the list, convert the current permutation into a tuple for it to be checkable in set
        #check if the current permutation is already in the set
        #if not, add it to both the set and the result list
        #for each index in the range from the current starting point to the end of the list, swap the elements to explore all permutations
        #recursively call backtrack with the next index to generate more permutations
        #after each call, swap the elements back to restore the original order before exploring the next permutations
        #return the list of unique permutations after all possible swaps and recursive calls are complete

        unique = set()
        res = []

        def backtrack(start):
            if start == len(nums):
                t = tuple(nums)
                if t not in unique:
                    unique.add(t)
                    res.append(nums[:])
                return
            for i in range(start, len(nums)):
                nums[start],nums[i] = nums[i],nums[start]
                backtrack(start + 1)
                nums[start],nums[i] = nums[i],nums[start]

        backtrack(0)

        return res