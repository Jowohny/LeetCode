from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        #create a counter to store the frequency of all the letters
        #store all the key value pairs in the dictionary into a list
        #convert the list into a max heap
        #pop all the values in the list and add the current letter by the amount of times it appeared until the heap is empty
        letterFreq = Counter(s)
        lfList = []
        res = ""


        for letter, freq in letterFreq.items():
            lfList.append((-freq, letter))
        
        heapq.heapify(lfList)

        while lfList:
            freq, letter = heapq.heappop(lfList)
            res += letter * -freq 
        
        return res
