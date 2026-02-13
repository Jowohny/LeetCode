class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        #initialize empty stack stack
        stack = []

        #pair numbers with their next greatest value
        nextGreatest = {}

        #interate through every item in nums2
        for n in nums2:

            #loop while there are items in the stack and the last item in the stack is less than the current number
            while stack and stack[-1] < n:

                #the stack represents the numbers that haven't found a number greater than itself
                #all items in the stack also come before the current number
                #since current number at this point is greater than the last item in the stack, this number can be considered the next greatest number for the last item in the stack, so we can create a key value pair within the nextGreatest dictionary
                nextGreatest[stack.pop()] = n

            #add the current number to the stack
            stack.append(n)

        #for all the other items in the left in the stack, it means that there weren't any number to the right of it that were greater than itself, we in the dictionary, we can assign each of the stack numbers a -1
        while stack:
            nextGreatest[stack.pop()] = -1

        #refer back to the nums1 list and create a another list using the values in the nums1 list as a key to reference their next greatest elemenet in the dictionary
        return [nextGreatest[n] for n in nums1]