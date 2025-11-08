class Solution:
    def countBits(self, n: int) -> List[int]:
        #from the range 0 to n, find the amount of 1 there are in each of their bit values
        #convert the current number to a binary and then use the count function to find how many ones there are
        #add the total amount of 1s for the current number then add to the list and return it once all numbers have been processed
        res = []
        for i in range(n+1):
            res.append(bin(i).count('1'))
        return res