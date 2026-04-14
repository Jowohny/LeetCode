class Solution:
    def mirrorFrequency(self, s: str) -> int:

        #create a whole string containing all the alphabet in order
        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        #create an entire dictionary that allows us to find each letter's or number's mirror
        mirrorDict = { alphabet[i]: alphabet[-i-1] for i in range(len(alphabet))} | {str(i): str(9 - i) for i in range(10) }

        #create a frequency list for the given string
        freq = collections.Counter(s)

        #use a set to avoid processing the same pair again
        seen = set()

        #add all distances to this variable
        distance = 0

        #loop through all items in the frequency counter
        for k, v in dict(freq).items():

            #only continue if the current letter or number hasn't been processed
            if k not in seen:

                #add the absolute value of the difference been the frequency of the current letter and the frequency of its mirror to the distance counter
                distance += abs(v - freq.get(mirrorDict[k], 0))

                #add both the current letter and its mirror to the list so we don't process its mirror later
                seen.add(k)
                seen.add(mirrorDict[k])

        #return the total distance found between the letters/numbers and their mirror counterparts
        return distance

