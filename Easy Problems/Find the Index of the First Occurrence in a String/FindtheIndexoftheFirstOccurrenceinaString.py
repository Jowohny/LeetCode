class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #check if the length of the needle is greater than the length of the stack
        #at every index, for the substring of the current index to the index + the length of the needle
        #check if that substring is equal to the needle
        #return the current index if the substring in the haystack is equal to the needle
        #if nothing is found then return -1

        if len(needle) > len(haystack):
            return -1
        elif needle == haystack:
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1