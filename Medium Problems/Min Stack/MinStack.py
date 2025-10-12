
class MinStack:
    #instead of keeping a stack of the actual values, stack the differences between them so its easy it indicate where on the stack introduced a new minimum
    #when pushing on to the stack, if there is no stack, the add the difference as 0 and set the minimum to the value added
    #if there is a stack, add the difference between the current value and the minimum, if the new value is less than the minimum, set new value to the minimum
    #if there isn't a stack to pop, return nothing
    #otherwise, pop the stack to get the latest difference and return that different added with the minimum to get the true value
    #also if the popped value happened to be a minimum, set it back to the previous minimum
    #to get the top of the stack, get the latest difference and add it to the minimum, if the difference happens to be negative, just return the minimum
    #just return the current minimum when calling for it
    #it is important to update our information along the way instead of traversing everytime to keep everything O(1)

    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        pop = self.stack.pop()

        if pop < 0:
            self.min -= pop

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()