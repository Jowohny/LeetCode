class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        #populate a list of the same length of the nums list with -1
        res = [-1] * len(nums)

        #initialize and empty stach
        stack = []

        #interate through the same list twice with their corresponding indexes to assimulate the curcular array
        for i, n in enumerate(nums+nums):

            #loop while there are items in the stack and number in the nums associated with the last index in the stack is less than the current number
            while stack and nums[stack[-1]] < n:

                #the stack contains all the indexes before this in ascending order
                #they also represent the indexes that havent found a number greater than its associated number
                #since the indexes in the stack also stand in for their place in the regular nums list, we can also use it to assume its place in the resulting array
                #using the last index in the stack, replace that index in the resulting list with the current number
                res[stack.pop()] = n
            
            #we only want to add numbers from the initial list, anything beyond the initial list is mainly for the 'circular' effect
            if i < len(nums):
                stack.append(i)

        #return the now modified list, any indexes that are still -1 are the numbers that are the greatest in the list since the greatest numbers can't have a greater element
        return res
