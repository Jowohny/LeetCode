class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        #create a default dictionary and default it with int(0)
        substrings = collections.defaultdict(int)


        #go through every substring of the minimum size in the given string
        for i in range(len(s)-minSize+1):

            #slice the string between the current index and the minimum size ahead of it
            curr = s[i:i+minSize]

            #only add the current substring if there are less than the max amount of letters we're supposed to have
            if len(set(curr)) <= maxLetters:
                substrings[curr] += 1

        if not substrings:
            return 0

        #go through the dictionary and find which of the substrings has the most occurances and return it
        return max(dict(substrings).values())
            