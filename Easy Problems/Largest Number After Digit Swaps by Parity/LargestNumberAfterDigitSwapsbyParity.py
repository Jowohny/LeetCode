class Solution:
    def largestInteger(self, num: int) -> int:
        #convert the number into a string to make it iterable
        digits = str(num)

        #seperate the digits into different lists based on their even or oddness
        #store the digits as negatives to create a max heap
        evens = [-int(d) for d in digits if int(d) % 2 == 0]
        odds  = [-int(d) for d in digits if int(d) % 2 == 1]

        heapq.heapify(evens)
        heapq.heapify(odds)

        #store the digits in a list to put back together later
        res = []

        #interate through the digits and check if the current number is even or odd
        #interate through the original number to keep the same order of parity numbers
        #pop the the respective heaps and negate value before adding to the resulting array
        for d in digits:
            if int(d) % 2 == 0:
                res.append(-heapq.heappop(evens))
            else:
                res.append(-heapq.heappop(odds))

        #convert all the numbers in the resulting array and join them together as a string in order, then convert to integer
        return int("".join(str(i) for i in res))