class Solution:
    def reverseWords(self, s: str) -> str:

        #split all words into a list
        wordList = s.split()

        #reverse the order of the list
        wordList = wordList[::-1]

        #join all the words in the reversed list with a space
        return ' '.join(wordList)