class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        #add onto the stack as we progress through each letter of the string
        stack = []

        #loop through each character in the given string
        for c in s:

            #only start checking once there are actually items in the stack
            #if the current character is the same as the last character in the stack, add 1 to the frequency of the last letter
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1

                #if the frequency of the last letter reaches k, remove that character from the stack
                if stack[-1][1] == k:
                    stack.pop()
            else:

                #if the current character is different from the last character in the stack, then add a new item onto the stack
                stack.append([c, 1])

        #create a list of using the letter and its frequency found in the stack
        res = [c*freq for c, freq in stack]

        #join all items in the resultant list into one single string
        return ''.join(res)

