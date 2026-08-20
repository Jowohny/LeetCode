class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #build a table where dp[i][j] answers does the first i characters of s match the first j characters of p
        #a '?' matches any single character, and a '*' matches any run of characters including an empty one
        #if the pattern character is a normal letter or a '?', this cell just leans on the diagonal, the match one step back on both strings
        #if the pattern character is a '*', it can either match nothing (look up) or swallow one more character of s (look left)
        #the bottom right corner of the table tells us if the whole string matches the whole pattern

        #dp table sized one bigger than each string to leave room for the empty prefixes
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        #an empty pattern matches an empty string
        dp[0][0] = True

        #an empty string can only be matched by a pattern of all stars, since each star can match nothing
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):

                #a matching letter or a '?' carries over whatever the diagonal cell decided
                if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]

                #a '*' matches nothing by looking up, or eats one character of s by looking left
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

        return dp[len(s)][len(p)]
