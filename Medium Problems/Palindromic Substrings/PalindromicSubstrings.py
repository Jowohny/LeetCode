class Solution:
    def countSubstrings(self, s: str) -> int:
        #use as a counter to track how many valid palindromic substrings
        res = 0

        #method to spread out from the given indexes
        def ripple(l,r):
            nonlocal res

            #increase the range by moving them in opposite directions
            #only continue moving pointers if they are in range and if the letters at both points remain the same
            while 0 <= l and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
        #start at every possible index
        for i in range(len(s)):

            #call twice with different variations
            #first call variation is for the palindromes that are of odd length
            #second variation is for the palindromes that are of even length
            ripple(i,i)
            ripple(i,i+1)

        #after rippling out from each index, return the total amount of palindromic substrings in the given string
        return res