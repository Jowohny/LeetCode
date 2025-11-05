class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        #for each row, add up all the values and append the value of the row alongside the index of that row to a list
        #convert that list into a heap
        #pop from the list k times and take the index of the popped items and append it to a seperate list
        #after there are k items in the new list, return the list
        rows = []
        res= []
        for i, l in enumerate(mat):
            rowSum = 0
            for n in l:
                rowSum += n
            rows.append([rowSum, i])
        heapq.heapify(rows)

        for i in range(k):
            row = heapq.heappop(rows)[1]
            res.append(row)
        return res
