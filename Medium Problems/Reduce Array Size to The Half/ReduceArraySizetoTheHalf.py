class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        #create a frequency list of all the numbers
        freq = collections.Counter(arr)

        #add all the numbers and invert their frequencies so the heap becomes a max heap
        heap = [-f for _,f in freq.items()]
        heapq.heapify(heap)

        #keep track of how many numbers we have removed from the heap as well as how much of list array numbers we have removed
        currSize = 0
        countUnique = 0

        #loop until at least half the array's worth of numbers have been removed
        while currSize < len(arr)//2:

            #pop off the number with the greatest frequency within the arr
            #add the frequency to the total amount of items removed and increment the amount of unique numbers removed
            f = heapq.heappop(heap)
            currSize -= f
            countUnique += 1

        #return the total amount of unique numbers removed from the list to get to half the size of the array
        return countUnique