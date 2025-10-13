class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #initialize a list of 0s, same length as the list of temperatures
        #use a stack to keep track of all the temperatures added that hasn't found a higher temperature than itself
        #append to every temperature to the stack one index at a time
        #enumerate the list of temperatures to keep the index for the resulting array
        #at every index, check whether the item at the top of the stack is less or higher than the current temperature
        #if its less than, add it to the stack since it needs to find another temperature greater than itself to be popped out
        #if greater than, pop all values in the stack that are less than the current temperature, find the difference between the current index and the index of the popped temperature and add to designated index in the result array
        #if by the end there are values left in the stack, by default the values at the temperature index in the result array are 0 due to how we initialized it

        res = [0] * len(temperatures)
        stack = []

        for index,temp  in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                sI,sT = stack.pop()
                res[sI] = index - sI
            stack.append([index, temp])
        return res

        