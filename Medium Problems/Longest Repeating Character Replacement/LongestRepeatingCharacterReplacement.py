class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #use a dictionary to keep track of all the letters along with their frequencies in the current window
        #use 2 pointers, one to iterate to find new letters, and the other to iterate when the current window is not valid 
        #loop through the string and add the current letter to the dictionary and icrements its frequency value
        #keep a max frequency value so we have access to the value throughout the loop and dont keep to search through the dictionary
        #our current window is considered invalid when the difference between the most frequent letter and the length of the list greater than the amount of letters we can change
        #at the end of every loop, find the max between the current window length and the max length overall

        counter = {}
        res = 0

        l = 0
        maxFreq = 0
        for r in range(len(s)):
            counter[s[r]] = 1 + counter.get(s[r], 0)
            maxFreq = max(maxFreq, counter[s[r]])

            while (r - l + 1) - maxFreq > k:
                counter[s[l]] -= 1
                l += 1
            
            res = max(res, (r - l + 1))
        return res