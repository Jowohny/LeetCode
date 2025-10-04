class Solution:
    def hIndex(self, citations: List[int]) -> int:
        #go through the list with a for loop
        #sort the citations
        #at every point, check if the current amount of citations are 
        #greater than or equal the length of the list afterwards
        #return the point in which the number of citations are more than the rest of the list
        #since it is sorted, it is ok to assume that the number of citations for the rest of
        #list is greater then the present point

        citations.sort()
        
        for i in range(len(citations)):
            if citations[i] >= len(citations)-i:
                return len(citations)-i
        return 0