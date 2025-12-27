from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        #create a frequency list for both words
        freq1 = Counter(s)
        freq2 = Counter(t)

        #interate through each letter and its frequency in the frequency list for the second word
        for k,v in freq2.items():

            #if the current letter isn't in the dictionary, give it a 0 value
            contain = freq1.get(k, 0)

            #if the current letter is marked as 0, or doesn't have the same frequency as the original list, then we need to return the current letter
            if contain != v or contain == 0:
                return k