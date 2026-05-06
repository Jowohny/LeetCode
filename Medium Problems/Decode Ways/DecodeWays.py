class Solution:
    def numDecodings(self, s: str) -> int:

        #create a cache array with an extra base value to keep the results how many ways we can decode substrings up to a certain point
        dp = [0] * (len(s)+1)

        #set the last element as 1 for the base case
        dp[len(s)] = 1


        #loop from the end of the list to the bottom
        for i in range(len(s)-1,-1,-1):

            #if the current value at the current index is 0, then we can't decode it since 0 isn't linked to any letter, so at this index, mark it as 0
            #if it is any other number, then then take the amount of ways the next number in the cache can be decoded and add it to itself
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] += dp[i+1]

            #do an initial check whether there is a next index after the current one, mainly for checks at the end of the list
            #check for any possible signs of a double digit decode
            #if the current number is 1, then any number after that (0-9) maps to a letter
            #if the current number is 2, then we would have to check if the number after is 0-6, since there are only 26 letters in the alphabet
            #if all comes out to be true, the current index is a double digit number that can be decoded into a letter, in that case, find the amount of decoded values from the cache 2 indexes ahead of the current one, since the current i and i+1 take up the space of the decoded value
            if i+1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i+1] in '0123456'):
                dp[i] += dp[i+2]

        #if the chance the the starting number is 0, the loop will take that into account and the index of 0 will be set as 0
        #otherwise it just takes into account the total amount of ways the given string can be decoded
        return dp[0]