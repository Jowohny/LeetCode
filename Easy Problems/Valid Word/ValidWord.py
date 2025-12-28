class Solution:
    def isValid(self, word: str) -> bool:

        #create a dictionary for vowel, if its a letter and its not in the dictionary, then its a consonant
        vowel = {'a':1, 'e':1, 'i':1, 'o':1, 'u':1}

        #meet conditions of at least a consonant and one vowel for valid words
        cCheck, vCheck = False, False
        
        #in the case that the length of the word is less than 3 characters
        if len(word) < 3:
            return False

        #iterate through each letter of the word
        for c in word:

            #check if the current character is either a number or letter, if it is neither then return false
            if not c.isalnum():
                return False
            else:
                
                #check if the current character is a letter
                #if the vowel is found to be a vowel, set the vowel check to true to symbolize the existance of a vowel
                #if the letter isn't a vowel, then set the consonant check to true for the same reasons
                if c.isalpha():
                    getVowel = vowel.get(c.lower(), 0)
                    if getVowel:
                        vCheck = True
                    else:
                        cCheck = True


        #if all letters were either a number or letter, had at least one consonant and one vowel, and had over 3 characters,
        return True if vCheck and cCheck else False