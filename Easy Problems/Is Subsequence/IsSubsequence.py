class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        #in the case the the first string is empty
        if not s:
            return True

        #use an index pointer to keep increment the through the letters as we find them in the second string to keep the order
        sp = 0

        #interate through the each of the letters in the second word
        for l in t:

            #if we find an instance of the current index of the first word in the second, increment the index to find the next letter
            if l == s[sp]:
                sp += 1

            #if at any point in the loop we see than the amount of letters match the length of the first string, the second string contains a subsequence of the first
            if len(s) == sp:
                return True

        #if we get through the entire loop, it means that there was no sufficient subsequence that was found
        return False