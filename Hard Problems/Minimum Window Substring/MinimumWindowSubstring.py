from collections import defaultdict, Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #use two hashmaps to track character frequencies, a counter for the populated t, and a default dictionary for the window
        #expand the window using for loop and update windowFreq based on the character of the right pointer
        #if the current character matches the required count from t, increase how much of much we have
        #when we have all the required letters, increase the index of the left pointer in search of a smaller valid window
        #update the minimum window length and starting index whenever a smaller valid window is found
        #keep shrinking the window by incrementing the left pointer and updating the frequency accordingly
        #return the smallest substring using the starting index updated through the loop with the minimum length we found
        #by the end if we see that the minimum length hasn't change from infinity, return an empty string as we found nothing

        if len(t) > len(s):
            return ""

        freqT, windowFreq = Counter(t),defaultdict(int)
        have,need = 0, len(freqT)
        sI,minLen = 0, float('inf')
        l = 0
        for r in range(len(s)):
            windowFreq[s[r]] += 1

            if s[r] in freqT and freqT[s[r]] == windowFreq[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < minLen:
                    sI = l
                    minLen = r - l + 1
                windowFreq[s[l]] -= 1
                if s[l] in freqT and windowFreq[s[l]] < freqT[s[l]]:
                    have -= 1
                l += 1

        if minLen != float('inf'):
            return s[sI:sI+minLen]
        else:
            return ""
                    
