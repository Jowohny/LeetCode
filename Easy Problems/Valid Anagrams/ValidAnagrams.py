from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #import counter
        #counter creates a dictionary with the frequency of all values
        #compare the frequency of all letters
        #if the frequency of all the letters are the same for both, then
        #they are valid anagrams

        return  Counter(s) == Counter(t)