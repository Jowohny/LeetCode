class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        #use a default dictionary to record all the frequencies as they are adjusted throughtout the problem
        numCount = collections.defaultdict(int)

        #use a heap to extract the number with the most frequency
        heap = []

        #use a list to add the frequency of the most recurring number at each step
        res = []
        
        #loop for every item in the combined list of the numbers and their respective frequencies
        for n, f in zip(nums, freq):

            #update the count of the current number frequency in the dictionary
            #since we need to extract the max, we subtract instead of add in order to create a max heap
            numCount[n] -= f

            #add the current number along with its frequency as the key
            heapq.heappush(heap, (numCount[n], n))

            #while there is a heap and the item at the top of the heap doesn't match the frequency recorded in the dictionary, remove it from the list as that heap item is not updated
            while heap and heap[0][0] != numCount[heap[0][1]]:
                heapq.heappop(heap)
            
            #if there are any items in the heap, add the first element in the heap as that will represent the largest, so add it to the resulting list
            res.append(-heap[0][0])

        #after all operations, return the final list with the all the most frequencies at each step
        return res