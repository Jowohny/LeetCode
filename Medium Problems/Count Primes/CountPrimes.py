class Solution:
    def countPrimes(self, n: int) -> int:

        #since 1 and 0 aren't prime numbers, if we have n as 1 or 0, we return 0
        if n < 2:
            return 0

        #create a boolean list with the first 2 indexes marked as non-prime(0) and the rest as prime(1) for now
        primes = [0] * 2 + [1] * (n-2)

        #start at index
        i = 2

        #loop while the squared value of the current index is less than the range of numbers
        while i**2 < n:

            #if the current index is still marked as prime, we can try to remove the multiples of the current index
            #if it was marked as non-prime, it might have already been marked as non-prime from a previous number
            if primes[i]:

                #iterate from the curret index to the end of the list and mark the multiples as non-prime
                for m in range(i**2, n, i):
                    primes[m] = 0

            #incrememt the index
            i += 1

        #since booleans can be marked as 0 and 1 for false and true, you can use sum to find out how many trues there are in a list
        return sum(primes) 
