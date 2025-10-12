class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #use a stack and convert all numbers in token to integers when appending to said stack
        #assume we won't have more than 2 items in the stack before finding the next operator
        #append new values to the stack based on the operation by popping both items in the list and performing the operation before adding back to the stack
        #everything is mostly normal besides the division, in which we need to convert it to a float then truncate it by converting it back to an int
        #return the only item in the stack which is the resultant number after all operations

        stack = []
        
        for n in tokens:
            if n == '+':
                stack.append(stack.pop() + stack.pop())
            elif n == '*':
                stack.append(stack.pop() * stack.pop())
            elif n == '-':
                n1,n2 = stack.pop(), stack.pop()
                stack.append(n2-n1)
            elif n == '/':
                n1,n2 = stack.pop(),stack.pop()
                stack.append(int(float(n2)/n1))
            else: 
                stack.append(int(n))
        return stack[0]