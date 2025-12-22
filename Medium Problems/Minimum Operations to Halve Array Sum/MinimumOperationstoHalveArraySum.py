class Solution:
    def halveArray(self, nums: List[int]) -> int:
        #track how many operations it takes to get to half the initial array value
        res = 0

        #create a negated version of the original array so it becomes a max heap when heapifying
        numList = [-n for n in nums]
        heapq.heapify(numList)

        #have a couple references to initial total sum and half the initial total sum
        initialTotal = sum(numList)
        halfTotal = initialTotal/2

        #loop until the intial total becomes less than half of what it used to be
        while initialTotal < halfTotal:

            #pop the highest value off the list, take away half of the popped value from the  initial total sum and push the half of the popped value back into the heap
            n = heapq.heappop(numList)
            initialTotal -= n/2
            heapq.heappush(numList, n/2)

            #each loop represents one operation
            res += 1
        
        #return the total amount of operations to reduce the total to at least half of what it was
        return res



