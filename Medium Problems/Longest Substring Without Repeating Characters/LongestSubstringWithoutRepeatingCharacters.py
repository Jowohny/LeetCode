class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #create 2 pointers, one indexed at the first letter and the other indexed right after
        #increment the second pointer until theres a duplicate found in the current substring
        #if theres a duplicate found, increment the first pointer until no duplicates are found
        #keep a max length variable to keep track of the longest substring as we are iterating

        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1

        maxLen = 0
        currLen = 0
        
        i,j = 0,0
        while i<len(s) and j<len(s):
            if s[j] in s[i:j]:
                if currLen > maxLen:
                    maxLen = currLen
                currLen -= 1
                i += 1
            elif s[j] not in s[i:j]:
                j += 1
                currLen += 1
            
        return max(maxLen, currLen)
