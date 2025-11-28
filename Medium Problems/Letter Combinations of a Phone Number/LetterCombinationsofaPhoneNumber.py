class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #make key value pairs so we know what letters belong to which digit
        numDict = {
            '2':'abc', '3':'def', '4':'ghi', '5':'jkl', 
            '6':'mno','7':'pqrs','8':'tuv','9':'wxyz'
        }

        #create a backtracking method to go through every possible string to be created by the given digits
        def backtrack(length, cur):
            #if the length of the current string reaches the amount of digits, then add them to the resulting list and stop
            if length == len(digits):
                result.append(cur)
                return
            
            #for every letter given by the current digit, add each letter to some variation of the combination
            for l in numDict[digits[length]]:
                #recall the method with added length and the new combination
                backtrack(length + 1, cur + l)

        #instantiate result list and do an initial call on the function
        result = []
        backtrack(0,"")

        #return the result list
        return resultclass Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #make key value pairs so we know what letters belong to which digit
        numDict = {
            '2':'abc', '3':'def', '4':'ghi', '5':'jkl', 
            '6':'mno','7':'pqrs','8':'tuv','9':'wxyz'
        }

        #create a backtracking method to go through every possible string to be created by the given digits
        def backtrack(length, cur):
            #if the length of the current string reaches the amount of digits, then add them to the resulting list and stop
            if length == len(digits):
                result.append(cur)
                return
            
            #for every letter given by the current digit, add each letter to some variation of the combination
            for l in numDict[digits[length]]:
                #recall the method with added length and the new combination
                backtrack(length + 1, cur + l)

        #instantiate result list and do an initial call on the function
        result = []
        backtrack(0,"")

        #return the result list
        return result