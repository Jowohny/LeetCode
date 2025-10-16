from collections import defaultdict

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        #define a dictionary with default values of one
        #create a result list that can later store all sequences of DNA that are repeated
        #create a window of size 10 and use the substring as the key for the dictionary
        #we go through every key in the sequence dictionary and add all strings to the list that have appeared in the DNA sequence twice or more to the result array
        
        sequence = defaultdict(int)
        res = []

        if len(s) < 10:
            return res

        l = 0
        for r in range(10, len(s)+1):
            key = s[l:r]
            sequence[key] += 1
            l += 1

        for key in sequence:
            if sequence[key] >= 2:
                res.append(key)
        return res