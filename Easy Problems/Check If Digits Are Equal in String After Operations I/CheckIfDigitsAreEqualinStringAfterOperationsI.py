class Solution:
    def hasSameDigits(self, s: str) -> bool:
        #while we have the original string at a length greater than 2, add each pair and create a new string
        #the new string is one less in length than the interation before this
        #we repeatedly add in pairs and reduce the length until we reach a length of 2
        #when we reach 2 length, compare both letters and return 
        while len(s) > 2:
            sm = ""
            for i in range(len(s) - 1):
                sm += str((int(s[i]) + int(s[i + 1])) % 10)
            s = sm
        return s[0] == s[1]