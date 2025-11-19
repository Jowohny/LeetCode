from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        #create a frequency list of all the values within the array
        #set the initial value to -1 in the case that there are no lucky values
        #run through the item's key value pairs found in the frequency list and if the key value pairs are equal to each other, then compare the current lucky value and either the key or value since they are the same in this context
        #after running through all items in the frequency list, return the lucky value
        freq = Counter(arr)
        lucky = -1
        
        for k,v in freq.items():
            if k == v:
                lucky = max(lucky, k)
                
        return lucky