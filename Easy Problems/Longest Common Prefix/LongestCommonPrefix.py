class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #sort all strings to bring lexicographically smallest and largest together
        #only compare the first and last word in the sorted list
        #because whatever prefix they share will be common to all others in between
        #check character by character while both are the same
        #return the prefix up to the point where they differ
        strs.sort()
        first = strs[0]
        last = strs[-1]
        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        return first[:i]
