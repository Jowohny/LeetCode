class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        #use a heap to organize the number pairs from greatest to least and keep another list to put the minimum number pairs into
        res = []
        heap = []

        #depending on which value is smaller, add all values in the first array with the first value in the second array along with their index and value in both lists, or push k of the values from the first list into the heap
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        #run this loop until the heap runs out of pairs to process or we've already popped k pairs and appended them to the result array
        while heap and k > 0:

            #pop from heap and unpack
            _, i, j = heapq.heappop(heap)

            #since we are in the heap, first k pairs of values will be have the small sum value, and the individual values to the list
            res.append([nums1[i], nums2[j]])
            k -= 1

            #if the index value from the second list is still within bounds, add the unpacked index value from the first list with the next index value from the second list and push it back onto the heap
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

        #return the resulting array after appending the k small sum value pairs into it
        return res
