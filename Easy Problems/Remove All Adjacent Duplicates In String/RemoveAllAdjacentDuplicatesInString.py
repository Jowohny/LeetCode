class Solution:
    def removeDuplicates(self, s: str) -> str:

        #initialize a stack to add items into as we explore the string
        stack = []

        #check each letter in the given string
        for char in s:

            #if the stack exist and the top of the stack is equal to the current letter, don't add the current letter and pop the same letter from the top of the stack
            #if either the stack doesn't exist or the letter isn't the same as the one on top of the stack, then add that current letter to the stack
            if stack and stack[-1]==char:
                stack.pop()
            else:
                stack.append(char)

        #use a stack mainly because strings are immutable and changing the string results in constant creations of more string
        #join the letters in the stack together to form the new string
        return "".join(stack)