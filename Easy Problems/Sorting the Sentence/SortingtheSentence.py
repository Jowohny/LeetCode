class Solution:
    def sortSentence(self, s: str) -> str:
        
        #split the sentence into its seperate words on each space
        words = s.split(' ')

        #create an array of strings the that is as long as the amount of words in the sentence
        res = [''] * len(words)

        #iterate through each word in the sentence
        for w in words:

            #seperate the order of the word and the word itself
            order, word = w[-1], w[:-1]

            #store the word in its exact place in the array
            res[int(order)-1] = word

        #combine all the words in the result array with a space in between them
        return ' '.join(res)