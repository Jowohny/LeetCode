class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        #create a frequency list of all the letters in the magazine
        freq = collections.Counter(magazine)

        #iterate through each letter in the ransomNote
        for l in ransomNote:

            #if the frequency of the current letter found in the dictionary is 0, that means there aren't enough letters to reconstruct the ransomNote, return False
            if freq[l] == 0:
                return False

            #take away 1 from the frequency to update how much of that letter we have left to recontruct
            freq[l] -= 1

        #if it goes through the whole loop, it means that we have enough letters to reconstruct the note
        return True