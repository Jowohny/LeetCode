class Solution:
    def firstUniqChar(self, s: str) -> int:
        #create a counter to relay how frequent each letter is in the string
        #for each letter in the string, go through the frequency dictionary with the character as the index
        #the first letter the has only one instance of itself in the string, return its current index
        #if nothing is found, then return -1
        freq = Counter(s)

        for i,c in enumerate(s):
            if freq[c] == 1:
                return i
        
        return -1