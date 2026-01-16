class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        #create a frequency list for all the stones
        stoneFreq = collections.Counter(stones)

        #create a set of all unique letters found in the jewel string
        jSet = set(jewels)

        #use this to accumulate the amount of stones
        totalStones = 0

        #only search for letters in the set
        for l in jSet:

            #add the frequency of the letter found in the stone frequency list
            totalStones += stoneFreq.get(l, 0)

        #return the total amount of jewels found in the stones
        return totalStones