class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #use a for loop to loop the length of the smaller string
        #for whatever string is longer, add the remaining string to the result
        #return the result lol
        res = ""
        for i in range(min(len(word1),len(word2))):
            res += word1[i]
            res += word2[i]

        if len(word1) > len(word2):
            res += word1[len(word2):]
        elif len(word1) < len(word2):
            res += word2[len(word1):]
        return res