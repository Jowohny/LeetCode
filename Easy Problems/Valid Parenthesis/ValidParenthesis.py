class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #create dictionary with predefined pairs
        #check if the stack is empty
        #pop the most recent bracket and referece the list for the matching opening bracket
        #and return false if those conditions are true
        #if there isn't a closing bracket, add to the stack
        #if the list is empty, then all brackets have been matched and return true


        stack = []

        pairs = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in pairs: 
                if not stack or stack.pop() != pairs[char]: 
                    return False
            else:  
                stack.append(char)

        return not stack