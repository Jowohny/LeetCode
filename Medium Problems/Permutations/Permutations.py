class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #use backtracking to generate all possible permutations from the given list
        #initialize a result list to store all valid permutations
        #swap numbers in place to form new combinations without extra space
        #when the start index reaches the end, it means a full permutation has been formed
        #make a copy of the current permutation and append it to the result list
        #after each recursive call, swap numbers back to restore the original order for the next path
        #continue this process until all possible orderings have been explored (for loop ends)

        def backtrack(start):
            if start == len(nums):
                res.append(nums[:])
                return
            
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        res = []
        backtrack(0)
        return res