class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        #store values we have already compiled so we don't have to repeat calculations
        power = {1: 0}

        #keep a list to store the power value and integer pairs
        res = []

        #helper function to compute power value using recursion
        def powerValues(num):

            #if the current number has already been memoized then call the key from the dictionary
            if num in power:
                return power[num]

            #depending on whether the current number is even or odd, perform the respective operations
            if num % 2 == 0:
                power[num] = 1 + powerValues(num // 2)
            else:
                power[num] = 1 + powerValues((3 * num) + 1)

            #return the power value
            return power[num]

        #calculate power values for all numbers in range
        for n in range(lo, hi + 1):
            res.append((powerValues(n), n))

        #since we have the power values set as the key in the pair, the results will be sorted by it
        res.sort()

        #return the value associated with the key at the kth value
        return res[k - 1][1]
