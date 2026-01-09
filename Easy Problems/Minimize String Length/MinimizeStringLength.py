class Solution:
    def minimizedStringLength(self, s: str) -> int:

        #using the rules, it is most likely the case that we can only have at most of 1 of each unique character
        #use a set to remove all duplicate characters
        #return the length of the set
        return len(set(s))