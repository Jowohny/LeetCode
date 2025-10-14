from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #if the length of the first string is greater than the second, then theres no way the second string can contain the first
        #use a counter to map the amount of each letter
        #populate another dictionary with the same amount of characters from the second string starting from index 0
        #check if the initial maps are equal, by then return True, otherwise continue
        #in a for loop, start the left side of the window at 0, and the right side from the index last found in in the second string
        #every interation, add the next letter and and remove the first one; iterate both sides so the length of the window stays constant
        #check the dictionarys at the end of each loop to see if they are equal

        if len(s1) > len(s2):
            return False

        s1map = Counter(s1)
        s2map = defaultdict(int)

        for i in range(len(s1)):
            s2map[s2[i]] += 1

        if s1map == s2map:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            s2map[s2[l]] -= 1
            s2map[s2[r]] += 1

            if s2map[s2[l]] == 0:
                del s2map[s2[l]]
            l += 1 
            if s1map == s2map:
                return True
        return False