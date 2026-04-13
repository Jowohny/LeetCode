class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        #create a frequency list for the current string of characters
        freq = collections.Counter(text)

        #only retrieve the letters necessary to make the word balloon
        #since we need 2 l's and 2 o's, divide their amount by 2
        return min(freq['b'], freq['a'], freq['l']//2, freq['o']//2, freq['n'])
        