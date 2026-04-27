class MyStack:

    def __init__(self):

        #initialize an empty deque
        self.q = deque()

    def push(self, x: int) -> None:

        #add the given value to the top of the deque
        self.q.append(x)

        #all the numbers left of the one we just added, pop them out from left to right and add them back into the deque so they appear to the right of the added number
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:

        #the 0th indexed item is represented as the 'top' of the stack, use the popleft deque method to pop the leftmost item from the deque
        return self.q.popleft()

    def top(self) -> int:

        #like mentioned before, the 0th indexed item in the deque is represented as the top, so find the value of the left most item in the deque and return the value
        return self.q[0]
        

    def empty(self) -> bool:

        #check the length of the deque, if it is equal to 0, then the 'stack' is currently empty, otherwise, it is non-empty
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()