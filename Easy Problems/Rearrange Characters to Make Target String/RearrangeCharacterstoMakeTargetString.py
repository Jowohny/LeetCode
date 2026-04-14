class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:

        #create counters for both the target and string
        freqS = collections.Counter(s)
        freqTarget = collections.Counter(target)

        #use a list to add only the required letters to compare later
        res = []

        #use a set to avoid adding the same letter multiple times
        seen = set()

        #iterate through each dictionary item for the target
        for k, v in dict(freqTarget).items():

            #only add the current letter into the list if it hasn't already been added 
            if k not in seen:

                #look in the counter made for the string for the amount of that letter
                #divide it by the amount of letters need by the target string
                res.append(freqS[k]//v)

                #add the current letter to the set so it doesn't get added again
                seen.add(k)

        #based off the list of the number of time the string meets the requirements of the target count, take the smallest amount as that is the total number of times to make the target from the string
        return min(res)

        

        