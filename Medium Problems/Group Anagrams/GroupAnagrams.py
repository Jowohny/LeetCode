from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create dictionary to keep track of all different anagrams
        #import counter to create frequency list
        #store each string with the frequency as the key
        #return everthing based on group anagrams
        gA = defaultdict(list)

        for s in strs:
            gA[''.join(sorted(s))].append(s)
        
        return list(gA.values())
