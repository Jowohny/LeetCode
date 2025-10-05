class Solution:
    def climbStairs(self, n: int) -> int:
        #for any n lower than 2, return n as it is already the amount of ways to go
        #the pattern to find how many steps is to see how many ways to arrange taking one or 2 steps
        #when taking one step, n - 1, when taking two steps, n - 2
        #by adding those together, it tells us how many steps remaining, in the same manner, this
        #also follows the fibonacci sequence

        if n <= 2:
            return n

        a, b = 1, 2
        for _ in range(n - 2):
            a, b = b, a + b
        return b
