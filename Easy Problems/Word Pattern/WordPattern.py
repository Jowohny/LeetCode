class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        #split the sentence up into a list of words
        words = s.split(' ')

        #if the number of letters in the pattern doesn't match the number of words, it's impossible
        if len(pattern) != len(words):
            return False
            
        #create a default dictionary with strings to map pattern letters to words
        pair = collections.defaultdict(str)

        #create a set to keep track of words that have already been assigned to a letter
        seen_words = set()

        #loop through every letter in the pattern
        for i in range(len(pattern)):

            # f the current pattern letter is empty, we need to assign it a word
            if pair[pattern[i]] == '':

                #if the word is already taken by another letter, then the pattern is invalid
                if words[i] in seen_words:
                    return False
                
                #assign the word to the pattern and mark the word as seen
                pair[pattern[i]] = words[i]
                seen_words.add(words[i])

            #if the pattern is already assigned, compare the stored word to the current word
            #if they don't match, return false as the pattern is broken
            elif pair[pattern[i]] != words[i]:
                return False
                
        #after checking every pair without a failure, return true
        return True