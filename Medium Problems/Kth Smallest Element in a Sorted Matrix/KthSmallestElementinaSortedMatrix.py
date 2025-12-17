class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        #predefine matrix side length for later reference and initialize heap
        rows,cols = len(matrix),len(matrix[0])
        heap = []

        #process every single value within the matrix
        for r in range(rows):
            for c in range(cols):

                #push the negative version of the value on the heap so the 8th smallest value is sitting on top of the heap 
                heapq.heappush(heap, -matrix[r][c])

                #if the heap has more characters then k, then pop the current kth smallest value on top of the heap
                if len(heap) > k:
                    heapq.heappop(heap)

        #return the negation of the value currently sitting on top of the heap
        return -heapq.heappop(heap)
            