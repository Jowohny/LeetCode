from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        #create a Counter to store all the frequencies of the letters
        freq = Counter(word)

        #for every different letter, remove one instance of it from the frequency
        for ch in freq:
            freq[ch] -= 1
            
            #add all the non zero frequencies of the remaining letters to the list
            remaining = []
            for f in freq.values():
                if f > 0:
                    remaining.append(f)

            #convert the remaining frequency list into a set, if the length of the set is 1, then all letters have equal frequency
            if len(set(remaining)) == 1:
                return True

            #add a frequency back to the letter to test other cases
            freq[ch] += 1 

        #return false if running through the enture frequency array with no true
        return False

        #changed comment style for now
