class Solution:
    def fib(self, n: int) -> int:
        #if nth number needed in the sequence is less than 2, then just return the number
        if n < 2:
            return n
        
        #use 2 numbers to keep track of the last 2 numbers in the sequence
        n1,n2 = 0,1

        #run this for n-1 times since we already know the first 2 numbers
        for _ in range(n-1):

            #n1 becomes n2 and and n2 becomes the sum of n1 and n2
            n1,n2 = n2,n1+n2

        #return n2 as that number will contain the final fibonacci
        return n2
            
