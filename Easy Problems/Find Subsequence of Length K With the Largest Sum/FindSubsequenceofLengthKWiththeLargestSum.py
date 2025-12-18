class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        #create a result list to store the sublist values and another to resort by their indexes
        res = []
        resort = []

        #create another list with the negated values along with their indexes to create a max heap with heapifying
        #storing with the value as the key makes it so the heap organizes by the number instead of its index
        maxHeap = [(-n, i) for i,n in enumerate(nums)]
        heapq.heapify(maxHeap)

        #pop k amount of values from the max heap and unnegate them back to their original for state to add the the resulting list
        #unpack the value and inverse the way it was stored in the max heap so we can sort it by the index to keep the original order
        for i in range(k):
            value, index = heapq.heappop(maxHeap)
            resort.append((index, -value))

        #sort the new list elements by their index
        resort.sort()

        #add solely the values from the newly sorted list into the final resulting list
        for _,v in resort:
            res.append(v)

        #return the resulting list
        return res