class Solution:
    def hIndex(self, citations: List[int]) -> int:
        #since we need to run O(log n), we can use binary search
        #we can check at the index of the mid point whether the current amount of 
        #citations there are greater than the remaining number of items in the list
        #and change the index of the pointers according
        #wait for the loop to finish and return the length of the list take away 
        #from left pointer index

        l,r = 0,len(citations)-1 

        while r >= l:
            m = (l+r)//2

            if citations[m] < len(citations) - m:
                l = m + 1
            else:
                r = m - 1
        return len(citations) - l