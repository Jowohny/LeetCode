class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        #create a seperate list of the same length of the original
        #store the value as a negative with its current index within the list so when we convert it to a heap, it creates a max heap
        #for the first 3 popped heap values, assign them to their respective medals and with their original place in the list
        #for every value after, label their original index in then new list as their place
        #return the new list of elements once the heap is empty
        rank = [0] * len(score)
        score = [(-val, i) for i,val in enumerate(score)]
        heapq.heapify(score)

        place = 1
        while score:
            i = heapq.heappop(score)[1]
            if place == 1:
                rank[i] = "Gold Medal"
            elif place == 2:
                rank[i] = "Silver Medal"
            elif place == 3:
                rank[i] = "Bronze Medal"
            else:
                rank[i] = str(place)
            place +=1
            
        return rank