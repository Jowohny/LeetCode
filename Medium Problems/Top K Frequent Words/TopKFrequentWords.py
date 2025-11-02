from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        #create a counter to put all words and its frequency into a dictionary
        #pair the frequency and the word associated with it into a max heap
        #pop the amount of items off the top of the list for k amount of times
        
        wordFreq = Counter(words)
        wfList = []
        res = []

        for word, freq in wordFreq.items():
            wfList.append((-freq, word))
        
        heapq.heapify(wfList)
        for i in range(k):
            res.append(heapq.heappop(wfList)[1])

        return res


        