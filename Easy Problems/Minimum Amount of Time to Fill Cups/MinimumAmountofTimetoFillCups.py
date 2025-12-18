class Solution:
    def fillCups(self, amount: List[int]) -> int:
        #keep count of how main different operations performed to get all cups filled
        res = 0
        
        #convert all values in the list to negatives so the list becomes a max heap
        cups = [-c for c in amount if c != 0]
        heapq.heapify(cups)

        #run this loop until all cups are fulled; when cups are filled they are removed from the list
        while len(cups) > 0:

            #get the 2 most cups that need the most filling and decrease the amount filled by 1
            cup1 = -heapq.heappop(cups)-1
            cup2 = -heapq.heappop(cups)-1 if len(cups) > 0 else 0

            #only add the cup back into the heap if it still needs filling
            if cup1 > 0:
                heapq.heappush(cups, -cup1)
            if cup2 > 0:
                heapq.heappush(cups, -cup2)

            #add 1 operation per loop
            res += 1

        #return the amount of operations after all cups are filled
        return res