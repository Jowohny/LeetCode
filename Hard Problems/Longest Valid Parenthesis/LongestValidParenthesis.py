class Solution:
    def longestValidParentheses(self, s: str) -> int:
        #initialize a stack to store indexes of invalid parenthesis, have stack index at -1 for dummy value
        #keep a variable to store the longest valid parenthesis length
        #iterate through every index and character in the string
        #if an open parenthesis is found, append its index to the stack
        #if a closing parenthesis is found, pop from the stack to close the last unmatched opening
        #if the stack becomes empty after popping, append the current index as the new base
        #if the stack is not empty, calculate the current valid length (difference between current index and top of the stack)
        #update the maximum length if the current valid length is longer
        #return the maximum length found after finishing the loop
        stack = [-1] 
        total = 0

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    total = max(total, i - stack[-1])

        return total