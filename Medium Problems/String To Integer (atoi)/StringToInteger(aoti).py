class Solution:
    def myAtoi(self, s: str) -> int:
        #check for any leading whitespace and ignore from final number
        #then check for a positive or negative sign and convert accordingly
        #while checking for numbers, we can check whether the current index is a digit
        #its important to check in order of empty space, then sign, then numbers in that order
        #since that was how it was specified and any other extra steps afterwards would 
        #guarantee an invalid number after that point
        #check if the number made is within the bounds of the contraints
        #convert all numbers in the end string to an int and return
        s = s.lstrip()
        if not s:
            return 0

        sign = 1
        i = 0
        res = 0

        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1

        res *= sign

        if res < -2**31:
            return -2**31
        if res > 2**31 - 1:
            return 2**31 - 1

        return res