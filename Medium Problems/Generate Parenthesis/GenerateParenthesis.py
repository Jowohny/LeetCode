class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #back tracking until there reaches a point in which the number of start and end parenthesis is equal to the amount of pairs
        #keep a stack variable to manage what is in the current interation during back tracking
        #add opening parenthesis on the conditions that there are more opening than closed or until the opening count has reached the number of pairs given
        #add closing parenthesis on the conditions that there has to be more opening than closing parenthesis
        #end back tracking on the condition that the number of both parenthesis are equal to the number of pairs
        #join all the current parenthesis in the stack and append to the resulting array
        #back track to other combinations until all possible valid combinations are complete

        stack = []
        res = []

        def backtrack(openP: int, closeP: int) -> None:
            if openP == closeP == n:
                res.append(''.join(stack))
                return
            
            if openP < n:
                stack.append('(')
                backtrack(openP + 1, closeP)
                stack.pop()
            
            if closeP < openP:
                stack.append(')')
                backtrack(openP, closeP + 1)
                stack.pop()
        
        backtrack(0,0)

        return res