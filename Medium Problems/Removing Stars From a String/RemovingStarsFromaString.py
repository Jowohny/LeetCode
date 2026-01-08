class Solution:
    def removeStars(self, s: str) -> str:
        
        #initialize stack to know the closest value to the next asterick
        stack = []

        #process each character in the string
        for c in s:

            #if there is at least 1 item in the stack and we find an asterick, then pop off the most recently processed character
            #if the character is a letter then just add it to the stack
            if stack and c == '*':
                stack.pop()
            else:
                stack.append(c)

        #join all the letter remaining in the stack into one string
        return ''.join(stack)