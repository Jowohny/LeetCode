class Solution:
    def reverse(self, x: int) -> int:
        #check if the value is negative
        #convert to string and reverse the string with indexing
        #multiply by negative if less than 0
        #check if the answer is within bounds of constraints
        
        res = 0

        if x < 0:
            res = int(str(x)[1:][::-1]) * -1
        else:
            res = int(str(x)[::-1])

        if res < (-1)*2**31 or res > 2**31-1:
            return 0

        return res